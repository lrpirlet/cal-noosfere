#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2021, Louis Richard Pirlet'
__docformat__ = 'restructuredtext en'

import socket
import datetime
from bs4 import BeautifulSoup as BS
from threading import Thread
import lxml

from calibre.ebooks.metadata.book.base import Metadata
from calibre.ebooks.metadata import check_isbn
from calibre.library.comments import sanitize_comments_html
from calibre.utils.cleantext import clean_ascii_chars
from calibre.utils.icu import lower

from calibre_plugins.noosfere import ret_soup, verify_isbn
from calibre_plugins.noosfere import noosfere


class Worker(Thread):
    # Get volume details, in a separate thread, from noosfere vol page from (book_url)s found in __init__

    def __init__(self, log, book_url, book_title, isbn, result_queue, browser, relevance, plugin, dbg_lvl, timeout=30):

        Thread.__init__(self)
        self.daemon = True
        self.log = log
        self.book_url = book_url
        self.nsfr_id = ""
        self.book_title = book_title
        self.isbn = isbn
        self.result_queue = result_queue
        self.br = browser.clone_browser()
        self.relevance = relevance
        self.plugin = plugin
        self.dbg_lvl = dbg_lvl
        self.timeout = timeout
        self.who="[worker "+str(relevance)+"]"
        self.from_encoding="windows-1252"
        self.extended_publisher = self.plugin.extended_publisher
        self.priority_handling = self.plugin.priority_handling
        self.must_be_editor = self.plugin.must_be_editor

        debug=self.dbg_lvl & 2
        self.log.info(self.who,"\nEntering worker")
        if debug:
            self.log.info(self.who,"self                  : ", self)
            self.log.info(self.who,"log                   : ", log)
            self.log.info(self.who,"book_url              : ", book_url)
            self.log.info(self.who,"book_title            : ", book_title)
            self.log.info(self.who,"isbn                  : ", isbn)
            self.log.info(self.who,"result_queue          : ", result_queue)
            self.log.info(self.who,"browser, self.browser : ", browser, self.br)
            self.log.info(self.who,"relevance             : ", relevance)
            self.log.info(self.who,"plugin                : ", plugin)
            self.log.info(self.who,"dbg_lvl               : ", dbg_lvl)
            self.log.info(self.who,"timeout               : ", timeout)
            self.log.info(self.who,"extended_publisher    : ", self.extended_publisher)
            self.log.info(self.who,"priority_handling     : ", self.priority_handling)
            self.log.info(self.who,"must_be_editor        : ", self.must_be_editor)

    def run(self):
        # wrk from __init__ could be a URL to the book (several volumes) or to the unique volume.
        # Sometimes we get a 'book' URL that is redirected to a 'volume' URL...
        # OK, il faut se connecter sur wrk_url et remonter url_vrai...
        # On décide sur url_vrai contenant niourf.asp (volume) ou ditionsLivre.asp (livre)
        #
        debug=self.dbg_lvl & 2
        self.log.info(self.who,"Entering run(self)")

        wrk_url = self.book_url
        if "ditionsLivre" in wrk_url:
            self.log.info("several volumes exist for this book")
            book_url="https://www.noosfere.org"+self.book_url+"&Tri=3"
            if debug: self.log.info(self.who,"book_url : ",book_url)
            try:
                wrk_url = self.ret_top_vol_indx(book_url, self.book_title)
                if debug: self.log.info(self.who,"wrk_url               : ", wrk_url)
            except:
                self.log.exception("ret_top_vol_indx failed for URL: ",book_url)

        if "niourf" in wrk_url:
            self.log.info("getting to THE volume for this book")
            vol_url="https://www.noosfere.org"+wrk_url.replace("./niourf","/livres/niourf")+"&Tri=3"
            if debug: self.log.info(self.who,"vol_url  : ",vol_url)
            try:
                self.extract_vol_details(vol_url)
            except:
                self.log.exception("extract_vol_details failed for URL: ",vol_url)

    def ret_top_vol_indx(self, url, book_title):
        # cette fonction reçoit l'URL du livre qui contient plusieurs volumes du même auteur,
        # dont certains ont le même ISBN et généralement le même titres.
        #
        # Ces volumes diffèrent par l'éditeur, la date d'édition ou de réédition, l'image de couverture, le 4me de couverture, la critique.
        # MON choix se base sur un système de points sur les indications du site
        # résumé présent:                       r   1pt
        # critique présente:                    c   1pt         # semble pas trop correct car CS n'existe pas même si, quand
        # critique de la série                  cs  1pt         # une critique existe, elle est reprise pour tous les volumes
        # sommaire des nouvelles présentes:     s   1pt
        # information vérifiée                  v   1pt
        # titre identique                       t   1pt
        # image présente                        p   1pt
        # isbn présent                          i  50pt         sauf préférence
        # isbn présent et identique a calibre     100pt         sauf préférence
        # le nombre de point sera  augmenté de telle manière a choisir le volume chez l'éditeur le plus représenté... MON choix
        # en cas d'égalité, le plus ancien reçoit la préférence
        #
        # This gets the book's URL, there many volume may be present with (or not) same ISBN, same title.
        # if the book only has one volume, then we bypass ret_top_vol_indx
        #
        # the volumes are different by the publisher, edition's or re-edition's date, cover, resume, critic...
        # MY choice is based on a point system based on the site's flag
        # resume available:                     r   1pt
        # critic available:                     c   1pt         # maybe incorrect as sometimes, when a critic exists
        # series critic:                        cs  1pt         # it is distributed to all volume without indication
        # summary of novel in the book:         s   1pt
        # verified information                  v   1pt
        # same title as requested               t   1pt
        # cover available                       p   1pt
        # isbn available                        i  50pt         unless overwritten by the priority choice
        # isbn available et same as requested     100pt         unless overwritten by the priority choice
        # the score will be increased so that the volume will be chosen to the most present publisher ... MY choice
        # in case of equality the oldest win
        #
        debug=self.dbg_lvl & 2
        self.log.info(self.who,"\nIn ret_top_vol_indx(self, url, title)")
        if debug:
            self.log.info(self.who,"url : ",url,", book_title : ",book_title)

        self.log.info(self.who,"calling ret_soup(log, dbg_lvl, br, url, rkt=None, who='[__init__]')")
        if debug:
            self.log.info(self.who,"url : ", url, "who : ", self.who)
        rsp = ret_soup(self.log, self.dbg_lvl, self.br, url, who=self.who)
        soup = rsp[0]
        url_vrai = rsp[1]
        if debug:
#            self.log.info(self.who,"top_vol_index soup :\n",soup)        # a bit long I guess
            self.log.info(self.who,"url_vrai  : ",url_vrai)

        if "niourf.asp" in url_vrai:
            self.log.info(self.who,"Bypassing to extract_vol_details, we have only one volume")
            return url_vrai.replace("https://www.noosfere.org","")                     #volume found return and set wrk_url to volume

        self.nsfr_id+= "bk$"+url_vrai.replace('?','&').replace('=','&').split('&')[2]
        if debug:
            self.log.info(self.who,"self.nsfr_id : ", self.nsfr_id)

        ts_vol_index={}
        # we like better volumes with an identifier, but some are edited on a particular publisher without isbn
        push_isbn = True if "isbn" in self.priority_handling else False
        if debug:
            self.log.info(self.who,"priority pushes isbn  : ", push_isbn)
            self.log.info(self.who,"priority balanced : ", bool( not "very" in self.priority_handling))

        nbr_of_vol=soup.select("td[class='item_bib']")
        for count in range(0,len(nbr_of_vol),2):
            subsoup=nbr_of_vol[count]
            point=0
            vol_index=vol_title=vol_cover_index=vol_editor=vol_isbn=vol_collection=""

            if subsoup.select("a[href*='numlivre']"): vol_index=subsoup.select("a[href*='numlivre']")[0]['href']

            if subsoup.select("a > img"): vol_title=subsoup.select("a > img")[0]['alt']
            if book_title.title()==vol_title.title():
                point+=1

            if subsoup.select("a > img"):
                vol_cover_index=subsoup.select("a > img")[0]['src']
                point+=1

            if subsoup.select("a[href*='numediteur']"): vol_editor=subsoup.select("a[href*='numediteur']")[0].text

            if subsoup.select("span[class='SousFicheNiourf']"):
                vol_isbn = subsoup.select("span[class='SousFicheNiourf']")[0].text.strip()
                vol_isbn = verify_isbn(self.log, self.dbg_lvl, vol_isbn, who=self.who)
                if vol_isbn:
                    if push_isbn:
                        point+=100
                        if self.isbn:
                            if verify_isbn(self.log, self.dbg_lvl, self.isbn, who=self.who)== vol_isbn: point+=100

            if subsoup.select("a[href*='collection']"): vol_collection=subsoup.select("a[href*='collection']")[0].text

            if subsoup.select("img[src*='3dbullgreen']"):
                point+=2

            tmp_presence=subsoup.select("span[title*='Présence']")
            if not "very" in self.priority_handling:
                for i in range(len(tmp_presence)):
                    if "R" in tmp_presence[i].text: point+=1
                    elif "C" in tmp_presence[i].text: point+=1
                    elif "CS" in tmp_presence[i].text: point+=1
                    elif "S" in tmp_presence[i].text: point+=1

            ts_vol_index[int(count/2)]=(point,vol_index,vol_editor)

            self.log.info(self.who,"found",int(count/2+1),"volumes différents")
            self.log.info(self.who,"key                   : ",int(count/2))
            self.log.info(self.who,"vol_index             : ",vol_index)
            self.log.info(self.who,"vol_title             : ",vol_title)
            self.log.info(self.who,"vol_cover_index       : ",vol_cover_index)
            self.log.info(self.who,"vol_editor            : ",vol_editor)
            self.log.info(self.who,"vol_isbn              : ",vol_isbn)
            self.log.info(self.who,"vol_collection        : ",vol_collection)
            self.log.info(self.who,"point                 : ",point)

        top_vol_point = 0
        top_vol_index = ""
        serie_editeur = []
        reverse_it = True if "latest" in self.priority_handling else False
        if debug: self.log.info(self.who,"priority pushes latest : ", reverse_it)

        # in python 3 a dict keeps the order of introduction... In this case, as noosfere presents it in chronological order,
        # let's invert the dict by sorting reverse if the latest volume is asked
        ts_vol_index = dict(sorted(ts_vol_index.items(),reverse=reverse_it))

        # create a list of publisher
        for key,ref in ts_vol_index.items():
            serie_editeur.append(ts_vol_index[key][2])

        # find the publishers in the list
        top_vol_editor={}.fromkeys(set(serie_editeur),0)

        # and set a value to each publisher function of the count and (the value of) self.must_be_editor
        for editr in serie_editeur:
            if self.must_be_editor:
                if self.must_be_editor == editr:
                    top_vol_editor[editr]+=10
                else:
                    top_vol_editor[editr]=1
            else:
                top_vol_editor[editr]+=1

        # compute all that and the final result is the first entry with the top number of point...
        for key,ref in ts_vol_index.items():
            if debug:
                self.log.info(self.who,"pour la clé", key,"la valeur des points est", ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]],"l'URL est",ts_vol_index[key][1],"l'éditeur est",ts_vol_index[key][2])
            if ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]>top_vol_point:
                top_vol_point=ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]
                top_vol_index=ts_vol_index[key][1]

        return top_vol_index

    def get_decoupage_annexe(self, dec_anx_url):
        # looks like we have some external ref to another series  of books for the same saga (different cut or even expansion to the series)
        # I want to catch it so I can get the info for the numbering
        #
        debug=self.dbg_lvl & 2
        self.log.info(self.who,"\nIget_decoupage_annexe(self, dec_anx_url)")
        if debug:
            self.log.info(self.who,"calling ret_soup(log, dbg_lvl, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"critic_url : ", dec_anx_url, "who : ", self.who)
        soup = ret_soup(self.log, self.dbg_lvl, self.br, dec_anx_url, who=self.who)[0]

        if debug:
#            self.log.info(self.who,"découpage annexe extract:\n",soup.select_one("div#Série").select_one("div").select_one("tbody").prettify())  # a bit long I guess
            self.log.info(self.who,"découpage annexe processed")

        return soup.select_one("div#Série").select_one("div").select_one("tbody")

    def get_Critique_de_la_serie(self, critic_url):
        # La critique de la série peut être développée dans une autre page dont seul l'URL est d'intérêt
        # cette fonction remplace le pointeur par le contenu.
        #
        # The critic for a series may be set apart in another page. The vol URL refers to that other location.
        # I want to have it.
        #
        debug=self.dbg_lvl & 2
        self.log.info(self.who,"\nIn get_Critique_de_la_serie(self, critic_url)")
        if debug:
            self.log.info(self.who,"calling ret_soup(log, dbg_lvl, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"critic_url : ", critic_url, "who : ", self.who)
        soup = ret_soup(self.log, self.dbg_lvl, self.br, critic_url, who=self.who)[0]

        if debug:
#            self.log.info(self.who,"critique de la série extract:\n","""soup.select_one('div[id="SerieCritique"]')""",soup.select_one('div[id="SerieCritique"]'))        # a bit long I guess
            self.log.info(self.who,"critique de la série processed")

        return soup.select_one('div[id="SerieCritique"]')

    def extract_vol_details(self, vol_url):
        # Here we extract and format the information from the choosen volume.
        # - The first name and last name to populate author and author sort : vol_auteur_prenom  and vol_auteur_nom
        # - The title of the volume                                         : vol_title
        # - The series name the volume is part of                           : vol_serie
        # - The sequence number in the serie                                : vol_serie_seq                         # missing
        # - The editor of this volume                                       : vol_editor
        # - The editor's collection of this volume                          : vol_coll
        # - The collection serial code of this volume                       : vol_coll_srl
        # - The "dépot légal" date (the publication date is vastly unknown) : vol_dp_lgl                            # date format to be computed
        # - The ISBN number associated with the volume                      : vol_isbn
        # - The volume tags                                                 : vol_genre
        # - The URL pointer to the volume cover image                       : vol_cover_index
        # - The comments includes various info about the book               : vol_comment_soup
        #   . reference, an URL pointer to noosfere
        #   . couverture, an URL pointer to noosfere, cover may be real small, but is accurate to the volume
        #   . first edition information
        #   . series (cycle) name and number
        #   . this volume editor info
        #   . Resume (quatrième de couverture)
        #   . Critiques
        #   . Sommaire detailing what novels are in the volume when it is an anthology
        #   . Critiques about the series and/or about another volume of the book
        #

        debug=self.dbg_lvl & 2
        self.log.info(self.who,"\nIn extract_vol_details(soup)")
        if debug:
            self.log.info(self.who,"vol_url       : ",vol_url)

        if debug:
            self.log.info(self.who,"calling ret_soup(log, dbg_lvl, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"vol_url : ", vol_url, "who : ", self.who)
        rsp = ret_soup(self.log, self.dbg_lvl, self.br, vol_url, who=self.who)
        soup = rsp[0]
        url_vrai = rsp[1].replace("&Tri=3","")
#        if debug: self.log.info(self.who,"extract_vol_details soup :\n",soup.prettify())              # a bit long I guess

        self.nsfr_id = self.nsfr_id+"$vl$"+url_vrai.replace('?','&').replace('=','&').split('&')[2]
      # self.nsfr_id = (self.nfsr_id).strip("$")                        # If I use this form, it gives this error: 'Worker' object has no attribute 'nfsr_id' ???
        tmp=self.nsfr_id
        self.nsfr_id=tmp.strip('$')

        if debug:
            self.log.info(self.who,"self.nsfr_id, type() : ", self.nsfr_id, type(self.nsfr_id))

        tmp_lst=[]
        vol_info={}
        vol_title=""
        vol_auteur=""
        vol_auteur_prenom=""
        vol_auteur_nom=""
        vol_serie=""
        vol_serie_seq=""
        vol_editor=""
        vol_coll=""
        vol_coll_srl=""
        vol_dp_lgl=""
        vol_isbn=""
        vol_genre=""
        vol_cover_index=""
        comment_generic=None
        comment_resume=None
        comment_Critiques=None
        comment_Sommaire=None
        comment_AutresCritique=None
        comment_cover=None
        comment_decoupage_annexe=None

        # add volume address as a reference in the comment
        vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"lxml")
        if debug: self.log.info(self.who,"vol reference processed")

        if soup.select("span[class='TitreNiourf']"): vol_title = soup.select("span[class='TitreNiourf']")[0].text.strip()
        if debug: self.log.info(self.who,"vol_title processed : ",vol_title)

        if soup.select("span[class='AuteurNiourf']"): vol_auteur = soup.select("span[class='AuteurNiourf']")[0].text.replace("\n","").strip()
        if debug: self.log.info(self.who,"vol_auteur processed : ",vol_auteur)
        for i in range(len(vol_auteur.split())):
            if not vol_auteur.split()[i].isupper():
                vol_auteur_prenom += " "+vol_auteur.split()[i]
            else:
                vol_auteur_nom += " "+vol_auteur.split()[i].title()
        vol_auteur = vol_auteur.title()
        vol_auteur_prenom = vol_auteur_prenom.strip()
        if debug: self.log.info(self.who,"vol_auteur_prenom processed : ",vol_auteur_prenom)
        vol_auteur_nom = vol_auteur_nom.strip()
        if debug: self.log.info(self.who,"vol_auteur_nom processed : ",vol_auteur_nom)

        if soup.select("a[href*='serie.asp']"):
            if soup.select("a[href*='serie.asp']")[0].find_parent("span", {"class":"ficheNiourf"}):
                vol_serie = soup.select("a[href*='serie.asp']")[0].text
                tmp_vss = [x for x in soup.select("a[href*='serie.asp']")[0].parent.stripped_strings]
                for i in range(len(tmp_vss)):
                    if "vol." in tmp_vss[i]:
                        if not vol_serie_seq:
                            vol_serie_seq=tmp_vss[i].replace("vol.","").strip()
                    if "découpage" in tmp_vss[i]:
                        dec_anx_url = "https://www.noosfere.org/livres/"+soup.select("a[href*='serie.asp']")[0]['href']
                        comment_pre_decoupage_annexe = BS('<div><p> </p><p style="font-weight: 600; font-size: 18px"> Découpage annexe</p><hr style="color:CCC;"/></div>',"lxml")
                        comment_decoupage_annexe = self.get_decoupage_annexe(dec_anx_url)
                if debug: self.log.info(self.who,"vol_serie, vol_serie_seq processed : ",vol_serie,",",vol_serie_seq)

        comment_generic = soup.select("span[class='ficheNiourf']")[0]
        new_div=soup.new_tag('div')
        comment_generic = comment_generic.wrap(new_div)
        if debug: self.log.info(self.who,"comment_generic processed")

        if soup.select("a[href*='editeur.asp']"): vol_editor = soup.select("a[href*='editeur.asp']")[0].text
        if debug: self.log.info(self.who,"vol_editor processed : ", vol_editor)

        if soup.select("a[href*='collection.asp']"): vol_coll = soup.select("a[href*='collection.asp']")[0].text
        if debug: self.log.info(self.who,"vol_coll : ", vol_coll)

        for i in comment_generic.stripped_strings:
            tmp_lst.append(str(i))
        vol_coll_srl = tmp_lst[len(tmp_lst)-1]
        if "n°" in vol_coll_srl:
            for k in ["n°","(",")"]:
                if k in vol_coll_srl:
                    vol_coll_srl=vol_coll_srl.replace(k,"")
            vol_coll_srl = vol_coll_srl.strip()
            vol_coll_srl = vol_coll_srl.split("/")[0]
            if vol_coll_srl[0].isnumeric(): vol_coll_srl=("0"*5+vol_coll_srl)[-6:]
        else:
            vol_coll_srl = ""
        if debug: self.log.info(self.who,"vol_coll_srl processed : ", vol_coll_srl)

        # publication date is largely ignored in noosfere, but we have the "dépot legal" date and I use it instead
        # note that I 'calculate' the missing day of the month and even sometimes the missing month
        ms=("janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre")
        for elemnt in soup.select_one("span[class='sousFicheNiourf']").stripped_strings:
            if debug: self.log.info(self.who,"elemnt : ", elemnt)
            if not vol_dp_lgl:
                elemn = (elemnt.replace("Dépôt légal :","").split(','))[0].strip()
                if elemn:
                    if elemn.isnumeric() and len(elemn) == 4:
                        vol_dp_lgl=datetime.datetime.strptime("175 "+elemn,"%j %Y")
                    elif "semestre" in elemn:
                        ele=elemn.split()
                        vol_dp_lgl=datetime.datetime.strptime(("000"+str((int(ele[0][0])-1)*175+97))[-3:]+" "+ele[2],"%j %Y")
                    elif "trimestre" in elemn:
                        ele=elemn.split()
                        vol_dp_lgl=datetime.datetime.strptime(("000"+str((int(ele[0][0])-1)*91+47))[-3:]+" "+ele[2],"%j %Y")
                    else:
                        for i in range(len(ms)):
                            if ms[i] in elemn:
                                ele=elemn.split()
                                vol_dp_lgl=datetime.datetime.strptime(("000"+str(10+31*i))[-3:]+" "+ele[1],"%j %Y")
                                break
                    if debug: self.log.info(self.who,"vol_dp_lgl : ", vol_dp_lgl)

            if "ISBN" in elemnt:
                vol_isbn = elemnt.lower().replace(" ","").replace('isbn:','')
                if "néant" in vol_isbn: vol_isbn=""
                if debug: self.log.info(self.who,"vol_isbn processed : ", vol_isbn)

            if "Genre" in elemnt:
                vol_genre = elemnt.lstrip("Genre : ")
                if debug: self.log.info(self.who,"vol_genre processed : ", vol_genre)

        if soup.select("img[name='couverture']"):
            for elemnt in repr(soup.select("img[name='couverture']")[0]).split('"'):
                if "http" in elemnt:
                    if not vol_cover_index:
                        vol_cover_index = elemnt
                        if debug: self.log.info(self.who,"vol_cover_index processed : ", vol_cover_index)

        # add cover image address as a reference in the comment
        if vol_cover_index:
            comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">'+ vol_cover_index +'</a></p></div>',"lxml")

    # select the fields I want... More exist such as film adaptations or references to advises to read
    # but that is not quite consistent around all the books (noosfere is a common database from many people)
    # and beside I have enough info like that AND I do NOT want to take out the noosfere's business

        tmp_comm_lst=soup.select("span[class='AuteurNiourf']")
        if debug: self.log.info(self.who,tmp_comm_lst)             #useful but too long
        for i in range(len(tmp_comm_lst)):
            if "Quatrième de couverture" in str(tmp_comm_lst[i]):
                comment_resume = tmp_comm_lst[i].find_parents("div",{'class':'sousbloc'})[0]
                if debug: self.log.info(self.who,"comment_resume processed")

            if "Critiques" in str(tmp_comm_lst[i]):
                if not "autres" in str(tmp_comm_lst[i]):
                    comment_Critiques = tmp_comm_lst[i].find_parents("div",{'class':'sousbloc'})[0]
                    if debug: self.log.info(self.who,"comment_Critiques processed")

            if "Sommaire" in str(tmp_comm_lst[i]):
                comment_Sommaire = tmp_comm_lst[i].find_parents("div",{'class':'sousbloc'})[0]
                if debug: self.log.info(self.who,"comment_Sommaire processed")

            if "Critiques des autres" in str(tmp_comm_lst[i]):
                comment_AutresCritique = tmp_comm_lst[i].find_parents("div",{'class':'sousbloc'})[0]

                if comment_AutresCritique.select('a[href*="serie.asp"]') and ("Critique de la série" in comment_AutresCritique.select('a[href*="serie.asp"]')[0].text):
                    critic_url = "https://www.noosfere.org/livres/"+comment_AutresCritique.select('a[href*="serie.asp"]')[0]['href']
                    try:
                        more_comment_AutresCritique=self.get_Critique_de_la_serie(critic_url)
                        comment_AutresCritique.append(more_comment_AutresCritique)
                    except:
                        self.log.exception("get_Critique_de_la_serie failed for url: ",critic_url)

                if debug: self.log.info(self.who,"comment_AutresCritique processed")


    # group in a big bundle all the fields I think I want... (It is difficult not to include more... :-))

        if comment_cover:
            vol_comment_soup.append(comment_cover)
        if comment_generic:
            vol_comment_soup.append(comment_generic)
        if comment_resume:
            vol_comment_soup.append(comment_resume)
        if comment_Critiques:
            vol_comment_soup.append(comment_Critiques)
        if comment_Sommaire:
            vol_comment_soup.append(comment_Sommaire)
        if comment_AutresCritique:
            vol_comment_soup.append(comment_AutresCritique)
        if comment_decoupage_annexe:
            vol_comment_soup.append(comment_pre_decoupage_annexe)     # this is the title
            vol_comment_soup.append(comment_decoupage_annexe)

    #
    # Make a minimum of "repair" over vol_comment_soup so that it displays correctly (how I like it) in the comments and in my catalogs
    # - I hate justify when it makes margin "float" around the correct position (in fact when space are used instead of absolute positioning)
    # - I like to have functional url when they exist
    # - I like to find out the next and/or previous books in a series (simulated arrows are link :-) )

        for elemnt in vol_comment_soup.select('[align="justify"]'):
            del elemnt['align']

    # remove all double or triple 'br' to improve presentation.
    # Note: tmp1 and tmp2 must contain a different value from any possible first element. (yes, I am lrp and I am unique :-) )
    #
    # ouais, et alors, si je modifie comment_generic APRES l'avoir intégré à vol_comment_soup, il n'y a qu'une seule version en mémoire...
    # donc vol_comment_soup est modifié...
    #

        tmp1=tmp2="lrp_the_unique"
        for elemnt in vol_comment_soup.findAll():
            tmp1,tmp2=tmp2,elemnt
            if tmp1==tmp2:
                elemnt.extract()

        br = soup.new_tag('br')
        for elemnt in vol_comment_soup.select('.AuteurNiourf'):
            elemnt.insert(0,br)
            elemnt["style"]="font-weight: 600; font-size: 18px"


        if debug:
            for elemnt in vol_comment_soup.select("a[href*='.asp']"):
                if 'http' not in elemnt.get('href'): self.log.info(self.who,"url incomplet avant correction: ", elemnt)

        for elemnt in vol_comment_soup.select("a[href*='/livres/auteur.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("/livres/auteur.asp","https://www.noosfere.org/livres/auteur.asp")
        for elemnt in vol_comment_soup.select("a[href*='/livres/niourf.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("/livres/niourf.asp","https://www.noosfere.org/livres/niourf.asp")
        for elemnt in vol_comment_soup.select("a[href*='/heberg/']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("/heberg/","https://www.noosfere.org/heberg/")

        for elemnt in vol_comment_soup.select("a[href*='./EditionsLivre.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("./EditionsLivre.asp","https://www.noosfere.org/livres/EditionsLivre.asp")
        for elemnt in vol_comment_soup.select("a[href*='./niourf.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("./niourf.asp","https://www.noosfere.org/livres/niourf.asp")
        for elemnt in vol_comment_soup.select("a[href*='heberg']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("../../heberg","https://www.noosfere.org/heberg")
        for elemnt in vol_comment_soup.select("a[href*='../bd']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("../bd","https://www.noosfere.org/bd")

        for elemnt in vol_comment_soup.select("a[href*='auteur.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("auteur.asp","https://www.noosfere.org/livres/auteur.asp")
        for elemnt in vol_comment_soup.select("a[href*='collection.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("collection.asp","https://www.noosfere.org/livres/collection.asp")
        for elemnt in vol_comment_soup.select("a[href*='critsign.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("critsign.asp","https://www.noosfere.org/livres/critsign.asp")
        for elemnt in vol_comment_soup.select("a[href*='EditionsLivre.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("EditionsLivre.asp","https://www.noosfere.org/livres/EditionsLivre.asp")
        for elemnt in vol_comment_soup.select("a[href*='editeur.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("editeur.asp","https://www.noosfere.org/livres/editeur.asp")
        for elemnt in vol_comment_soup.select("a[href*='editionslivre.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("editionslivre.asp","https://www.noosfere.org/livres/editionslivre.asp")
        for elemnt in vol_comment_soup.select("a[href*='niourf.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("niourf.asp","https://www.noosfere.org/livres/niourf.asp")
        for elemnt in vol_comment_soup.select("a[href*='serie.asp']"):
            if 'http' not in elemnt.get('href'): elemnt["href"]=elemnt["href"].replace("serie.asp","https://www.noosfere.org/livres/serie.asp")

        if debug:
            for elemnt in vol_comment_soup.select("a[href*='.asp']"):
                if 'http' not in elemnt.get('href'): self.log.info(self.who,"url incomplet apres correction: ", elemnt)

        fg,fd="<<==","==>>" #chr(0x21D0),chr(0x21D2)   #chr(0x27f8),chr(0x27f9)
        for elemnt in vol_comment_soup.select("img[src*='arrow_left']"): elemnt.replace_with(fg)
        for elemnt in vol_comment_soup.select("img[src*='arrow_right']"): elemnt.replace_with(fd)

        # depending on the tick box, make a fat publisher using separators that have a very low probability to pop up (§ and €)
        # only set vol_coll_srl if vol_coll exists
        # the idea is to use search and replace in the edit Metadata in bulk window.

        if self.extended_publisher:
            if debug: self.log.info(self.who,"""flag : "Ajoute collection et son numéro d'ordre au champ èditeur" set""")
            if vol_coll:
                if debug: self.log.info(self.who,'add collection')
                vol_editor = vol_editor+('§')+vol_coll
                if vol_coll_srl:
                    if debug: self.log.info(self.who,'add collection number')
                    vol_editor = vol_editor+('€')+vol_coll_srl

        if vol_serie:
            if vol_serie_seq.isnumeric(): vol_serie_seq = float(vol_serie_seq)
            else: vol_serie_seq = 1.0

        # UTF-8 characters may be serialized different ways, only xmlcharrefreplace produces xml compatible strings
        # any other non ascii character with another utf-8 byte representation will make calibre behave with the messsage:
        # ValueError: All strings must be XML compatible: Unicode or ASCII, no NULL bytes or control characters
        # Side note:
        # I have no real good URL structure(i once got html 3 times, div a sibling of html...), but calibre does not seems to care (nice :-) )
        #
        # Ça m'a pris un temps fou pour trouver, par hasard, que encode('ascii','xmlcharrefreplace') aidait bien...
        # (enfin, quasi par hasard, j' ai essayé tout ce qui pouvait améliorer la compatibilité avec xml... mais je
        # lisais mal et je pensais à une incompatibilité avec la structure xml),
        #
        vol_comment_soup = vol_comment_soup.encode('ascii','xmlcharrefreplace')

        self.log.info(self.who,"+++"*25)
        self.log.info(self.who,"nsfr_id, type()                : ",self.nsfr_id, type(self.nsfr_id))                    # must be <class 'str'>
        self.log.info(self.who,"relevance, type()              : ",self.relevance, type(self.relevance))            # must be <class 'float'>
        self.log.info(self.who,"vol_title, type()              : ",vol_title, type(vol_title))                      # must be <class 'str'>
        self.log.info(self.who,"vol_auteur, type()             : ",vol_auteur, type(vol_auteur))                    # must be <class 'list'> of <class 'str'>
        self.log.info(self.who,"vol_auteur_prenom, type()      : ",vol_auteur_prenom, type(vol_auteur_prenom))      # must be <class 'str'>
        self.log.info(self.who,"vol_auteur_nom, type()         : ",vol_auteur_nom, type(vol_auteur_nom))            # must be <class 'str'>
        if vol_serie:
            self.log.info(self.who,"vol_serie, type()              : ",vol_serie, type(vol_serie))                  # must be <class 'str'>
            self.log.info(self.who,"vol_serie_seq, type()          : ",vol_serie_seq, type(vol_serie_seq))          # must be <class 'float'>
        self.log.info(self.who,"vol_editor, type()             : ",vol_editor, type(vol_editor))                    # must be <class 'str'>
        self.log.info(self.who,"vol_coll, type()               : ",vol_coll, type(vol_coll))                        # must be <class 'str'>
        self.log.info(self.who,"vol_coll_srl, type()           : ",vol_coll_srl, type(vol_coll_srl))                # must be <class 'str'>
        self.log.info(self.who,"vol_dp_lgl, type()             : ",vol_dp_lgl, type(vol_dp_lgl))                    # must be <class 'datetime.datetime'> ('renderer=isoformat')
        self.log.info(self.who,"vol_isbn, type()               : ",vol_isbn, type(vol_isbn))                        # must be <class 'str'>
        self.log.info(self.who,"vol_genre, type()              : ",vol_genre, type(vol_genre))                      # must be <class 'list'> of <class 'str'>
        self.log.info(self.who,"vol_cover_index, type()        : ",vol_cover_index, type(vol_cover_index))          # must be
        self.log.info(self.who,"type(vol_comment_soup)         : ",type(vol_comment_soup))                          # must be byte encoded (start with b'blablabla...
#        self.log.info(self.who,"vol_comment_soup               :\n",vol_comment_soup)                                # Maybe a bit long sometimes
                                                                                                               # language must be <class 'str'>

        if vol_cover_index:
            self.plugin.cache_identifier_to_cover_url(self.nsfr_id, vol_cover_index)

        if vol_isbn:
            self.plugin.cache_isbn_to_identifier(vol_isbn, self.nsfr_id)


        mi = Metadata(vol_title, [vol_auteur])
        mi.set_identifier('nsfr_id', self.nsfr_id)
        mi.publisher = vol_editor
        mi.isbn = vol_isbn
        mi.tags = [vol_genre]
        mi.source_relevance = self.relevance
        mi.has_cover = bool(vol_cover_index)
        if vol_dp_lgl:
            mi.pubdate = vol_dp_lgl
        if vol_serie:
            mi.series = vol_serie
            mi.series_index = vol_serie_seq
        mi.language = "fra"

        mi.comments = vol_comment_soup

        if debug: self.log.info(self.who,"mi\n",mi,"\n")
        self.plugin.clean_downloaded_metadata(mi)

        self.result_queue.put(mi)
