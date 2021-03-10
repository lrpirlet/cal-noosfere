
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

from calibre_plugins.noosfere import ret_soup


class Worker(Thread):
    # Get volume details, in a separate thread, from noosfere vol page from (book_url)s found in __init__


    def __init__(self, log, book_url, lrpid, book_title, isbn, result_queue, browser, relevance, plugin, timeout=30):

        debug=1

        Thread.__init__(self)
        self.daemon = True
        self.log = log
        self.book_url = book_url
        self.lrpid = lrpid
        self.book_title = book_title
        self.isbn = isbn
        self.result_queue = result_queue
        self.br = browser.clone_browser()
        self.relevance = relevance
        self.plugin = plugin
        self.timeout = timeout
        self.who="[worker "+str(relevance)+"]"
        self.from_encoding="windows-1252"

        self.log.info("\nEntering worker", relevance)
        if debug:
            self.log.info(self.who,"self                  : ", self)
            self.log.info(self.who,"log                   : ", log)
            self.log.info(self.who,"book_url              : ", book_url)
            self.log.info(self.who,"lrpid                 : ", lrpid)
            self.log.info(self.who,"book_title            : ", book_title)
            self.log.info(self.who,"isbn                  : ", isbn)
            self.log.info(self.who,"result_queue          : ", result_queue)
            self.log.info(self.who,"browser, self.browser : ", browser, self.br)
            self.log.info(self.who,"relevance             : ", relevance)
            self.log.info(self.who,"plugin                : ", plugin)
            self.log.info(self.who,"timeout               : ", timeout)

    def run(self):
        # wrk from __init__ could be a url to the book (several volumes) or to the unique volume.
        # Sometimes we get a 'book' url that is redirected to a 'volume' url...
        # OK, il faut se connecter sur wrk_url et remonter url_vrai...
        # On decide sur url_vrai contenant niourf.asp (volume) ou ditionsLivre.asp (livre)
        #
        debug=1
        self.log.info(self.who,"Entering run(self)")

        wrk_url = self.book_url
        if "ditionsLivre" in wrk_url:
            book_url="https://www.noosfere.org"+self.book_url+"&Tri=3"
            if debug: self.log.info(self.who,"book_url : ",book_url)
            try:
                wrk_url = self.ret_top_vol_indx(book_url, self.book_title)
                if debug: self.log.info(self.who,"wrk_url               : ", wrk_url)
            except:
                self.log.exception("ret_top_vol_indx failed for url: ",book_url)

        if "niourf" in wrk_url:
            vol_url="https://www.noosfere.org"+wrk_url.replace("./niourf","/livres/niourf")+"&Tri=3"
            if debug: self.log.info(self.who,"vol_url  : ",vol_url)
            try:
                self.extract_vol_details(vol_url)
            except:
                self.log.exception("extract_vol_details failed for url: ",vol_url)


    def verify_isbn(self, isbn_str):
        # isbn_str est brute d'extraction... la fonction renvoie un isbn correct ou "invalide"
        # Notez qu'on doit supprimr les characteres de separation et les characteres restants apres extraction
        # et que l'on traite un mot de 10 ou 13 characteres.
        #
        # isbn_str is strait from extraction... function returns an ISBN maybe correct ...or not
        # Characters irrelevant to ISBN and separators inside ISBN must be removed,
        # the resulting word must be either 10 or 13 characters long.
        #
        debug=0
        self.log.info(self.who,"\nIn verify_isbn(isbn_str)")
        if debug:
            self.log.info(self.who,"isbn_str         : ",isbn_str)

        for k in ['(',')','-',' ']:
            if k in isbn_str:
                isbn_str=isbn_str.replace(k,"")
        if debug:
            self.log.info(self.who,"isbn_str cleaned : ",isbn_str)
            self.log.info(self.who,"return from verify_isbn\n")

        return check_isbn(isbn_str)         # calibre does the check for me after cleaning...

    def ret_top_vol_indx(self, url, book_title):
        # cette fonction reçoit l'url du livre qui contient plusieur volumes du meme auteur,
        # dont certains ont le meme ISBN et generalement le meme titres.
        #
        # This gets the book's url, there many volume may be present with (or not) same ISBN, same title.
        # if the book only has one volume, then we bypass ret_top_vol_indx
        #
        # Ces volumes diffèrent par l'editeur, la date d'edition ou de réédition, l'image de couverture, le 4me de couverture, la critique.
        # MON choix se base sur un systeme de points:
        # résumé présent:                       r   1pt
        # critique présente:                    c   1pt         # semble pas trop correct car CS n'existe pas meme si, quand
        # critique de la serie                  cs  1pt         # une critique existe, elle est reprise pour tous les volumes
        # sommaire des nouvelles presentes:     s   1pt
        # information verifiée                  v   1pt
        # titre identique                       t   1pt
        # image presente                        p   1pt
        # isbn present                          i   50pt
        # le nombre de point sera  augmenté de telle manière a choisir le livre chez l'éditeur le plus representé... MON choix
        # en cas d'egalité, le plus ancien reçoit la préférence
        # plus tard, je pense visualiser, par volume, une image et les charateristiques du volume avec un bouton de selection
        debug=1
        self.log.info(self.who,"\nIn ret_top_vol_indx(self, url, title)")
        if debug:
            self.log.info(self.who,"url : ",url,", book_title : ",book_title)

##        sr=self.br.open(url,timeout=20)
##        soup = BS(sr, "html5lib",from_encoding=self.from_encoding)

        self.log.info(self.who,"calling ret_soup(log, br, url, rkt=None, who='[__init__]')")
        if debug:
            self.log.info(self.who,"url : ", url, "who : ", self.who)
        rsp = ret_soup(self.log, self.br, url, who=self.who)
        soup = rsp[0]
        url_vrai = rsp[1]
        if debug:
#            self.log.info(self.who,"soup :\n",soup)        a bit long I guess
            self.log.info(self.who,"url_vrai  : ",url_vrai)

        if "niourf.asp" in url_vrai:
            self.log.info(self.who,"Bypassing to extract_vol_details, we have only one volume")
            self.extract_vol_details(url_vrai)

        ts_vol_index={}

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
                vol_isbn = self.verify_isbn(vol_isbn)
                if vol_isbn:
                    point+=500
                    if self.isbn:
                        if self.verify_isbn(self.isbn)== vol_isbn: point+=1000

            if subsoup.select("a[href*='collection']"): vol_collection=subsoup.select("a[href*='collection']")[0].text

            if subsoup.select("img[src*='3dbullgreen']"):
                point+=2

            tmp_presence=subsoup.select("span[title*='Présence']")
            for i in range(len(tmp_presence)):
                if "R" in tmp_presence[i].text: point+=1
                elif "C" in tmp_presence[i].text: point+=1
                elif "CS" in tmp_presence[i].text: point+=1
                elif "S" in tmp_presence[i].text: point+=1

        # lrp todo?? Ce choix constitue un racourci qui devrait etre remplacé par une presentation à l'utilisateur pour qu'il choisisse
        # problem:  autogrouping of similar books...
        #           how could we know if mass sourcing or one book sourcing?

            ts_vol_index[str(int(count/2))]=(point,vol_index,vol_editor)


            self.log.info(self.who,"found",int(count/2+1),"volumes différents")
            self.log.info(self.who,"key                   : ",str(int(count/2)))
            self.log.info(self.who,"vol_index             : ",vol_index)
            self.log.info(self.who,"vol_title             : ",vol_title)
            self.log.info(self.who,"vol_cover_index       : ",vol_cover_index)
            self.log.info(self.who,"vol_editor            : ",vol_editor)
            self.log.info(self.who,"vol_isbn              : ",vol_isbn)
            self.log.info(self.who,"vol_collection        : ",vol_collection)
            self.log.info(self.who,"point                 : ",point)

        top_vol_point,top_vol_index,serie_editeur=0,"",[]

        for key,ref in ts_vol_index.items():
            serie_editeur.append(ts_vol_index[key][2])

        top_vol_editor={}.fromkeys(set(serie_editeur),0)

        for editr in serie_editeur:
            top_vol_editor[editr]+=1

        for key,ref in ts_vol_index.items():
            if debug: self.log.info(self.who,"La clé est", key,"la valeur des points est", ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]],"le pointeur est",ts_vol_index[key][1],"l'éditeur est",ts_vol_index[key][2])
            if ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]>top_vol_point:
                top_vol_point=ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]
                top_vol_index=ts_vol_index[key][1]

        return top_vol_index

    def get_decoupage_annexe(self, dec_anx_url):
        # looks like we have some external ref to another series (different cut or even expantion) of book for the same saga
        # I want to catch it so I can get the info for the numbering
        #
        debug=1
        self.log.info(self.who,"\nIget_decoupage_annexe(self, dec_anx_url)")
        if debug:
            self.log.info(self.who,"calling ret_soup(log, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"critic_url : ", dec_anx_url, "who : ", self.who)
        soup = ret_soup(self.log, self.br, dec_anx_url, who=self.who)[0]

        if debug:
#            self.log.info(self.who,soup.select_one("div#Série").select_one("div").select_one("tbody").prettify())  #long
            self.log.info(self.who,"découpage annexe found")
        
        return soup.select_one("div#Série").select_one("div").select_one("tbody")

    def get_Critique_de_la_serie(self, critic_url):
        # La critique de la serie peut etre developpée dans une autre page dont seul l(url est d'interet
        # cette fondtion remplce le pointeur par le contenu.
        #
        # The critic for a serie may be set appart in another page. The vol url refers to that other loacation.
        # I want to have it local to my volume.
        #
        debug=1
        self.log.info(self.who,"\nIn get_Critique_de_la_serie(self, critic_url)")
        if debug:
            self.log.info(self.who,"calling ret_soup(log, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"critic_url : ", critic_url, "who : ", self.who)
        soup = ret_soup(self.log, self.br, critic_url, who=self.who)[0]

        if debug:
#            self.log.info(self.who,"""soup.select_one('div[id="SerieCritique"]')""",soup.select_one('div[id="SerieCritique"]'))        # trop grand, mais peut servir
            self.log.info(self.who,"critique de la serie found")

        return soup.select_one('div[id="SerieCritique"]')

    def extract_vol_details(self, vol_url):
        # Here we extract and format the information from the choosen volume.
        # - The first name and last name to populate author and author sort : vol_auteur_prenom  and vol_auteur_nom
        # - The title of the volume                                         : vol_title
        # - The serie name the volume is part of                            : vol_serie
        # - The sequence number in the serie                                : vol_serie_seq                         # missing
        # - The editor of this volume                                       : vol_editor
        # - The editor's collection of this volume                          : vol_coll
        # - The collection number of this volume                            : vol_coll_nbr
        # - The "dépot légal" date (the publication date is vastly unknown) : vol_dp_lgl                            # date format to be computed
        # - The ISBN number assoi-ciated with the volume                    : vol_isbn
        # - The volume tags                                                 : vol_genre
        # - The url pointer to the volume cover image                       : vol_cover_index
        # - The comments includes various info about the book               : vol_comment_soup
        #   . reference, an url pointer to noosfere
        #   . couverture, an url pointer to noosfere, cover may be real smal, but is accurate to the volume
        #   . first edition information
        #   . serie (cycle) name and number
        #   . this volume editor info
        #   . Resume (quatrième de couverture)
        #   . Critiques
        #   . Sommaire detailing what novels are in the volume when it is an anthology
        #   . Critiques about the serie and/or about another volume of the book
        #

        debug=1
        self.log.info(self.who,"\nIn extract_vol_details(soup)")
        if debug:
            self.log.info(self.who,"vol_url       : ",vol_url)

        if debug:
            self.log.info(self.who,"calling ret_soup(log, br, url, rkt=None, who='[__init__]')")
            self.log.info(self.who,"vol_url : ", vol_url, "who : ", self.who)
        rsp = ret_soup(self.log, self.br, vol_url, who=self.who)
        soup = rsp[0]
        url_vrai = rsp[1]
#        if debug: self.log.info(self.who,soup.prettify())              # useful but too big...

        tmp_lst=[]
        vol_info={}
        vol_title=vol_auteur=vol_auteur_prenom=vol_auteur_nom=vol_serie=vol_serie_seq=vol_editor=vol_coll=vol_coll_nbr=vol_dp_lgl=vol_isbn=vol_genre=vol_cover_index=""
        comment_generic=comment_resume=comment_Critique=comment_Sommaire=comment_AutresCritique=comment_cover=comment_decoupage_annexe=None

        vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"lxml")
        if debug: self.log.info(self.who,"vol reference found")

        if soup.select("span[class='TitreNiourf']"): vol_title = soup.select("span[class='TitreNiourf']")[0].text.strip()
        if debug: self.log.info(self.who,"vol_title found")

        if soup.select("span[class='AuteurNiourf']"): vol_auteur = soup.select("span[class='AuteurNiourf']")[0].text.replace("\n","").strip()
        if debug: self.log.info(self.who,"vol_auteur found")
        for i in range(len(vol_auteur.split())):
            if not vol_auteur.split()[i].isupper():
                vol_auteur_prenom += " "+vol_auteur.split()[i]
            else:
                vol_auteur_nom += " "+vol_auteur.split()[i].title()
        vol_auteur = vol_auteur.title()
        vol_auteur_prenom = vol_auteur_prenom.strip()
        if debug: self.log.info(self.who,"vol_auteur_prenom found")
        vol_auteur_nom = vol_auteur_nom.strip()
        if debug: self.log.info(self.who,"vol_auteur_nom found")

        if soup.select("a[href*='serie.asp']"):
            if soup.select("a[href*='serie.asp']")[0].find_parent("span", {"class":"ficheNiourf"}):
                vol_serie = soup.select("a[href*='serie.asp']")[0].text
                tmp_vss = [x for x in soup.select("a[href*='serie.asp']")[0].parent.stripped_strings]
                for i in range(len(tmp_vss)):
                    if "vol." in tmp_vss[i]:
                        vol_serie_seq=tmp_vss[i].replace("vol.","").strip()
                    if "découpage" in tmp_vss[i]:
                        dec_anx_url = "https://www.noosfere.org/livres/"+soup.select("a[href*='serie.asp']")[0]['href']
                        comment_pre_decoupage_annexe = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px"> (découpage annexe) </p></div>',"lxml")
                        comment_decoupage_annexe = self.get_decoupage_annexe(dec_anx_url)
                if debug: self.log.info(self.who,"vol_serie, vol_serie_seq found")

        comment_generic = soup.select("span[class='ficheNiourf']")[0]
        new_div=soup.new_tag('div')
        comment_generic = comment_generic.wrap(new_div)
        if debug: self.log.info(self.who,"comment_generic found")

        if soup.select("a[href*='editeur.asp']"): vol_editor = soup.select("a[href*='editeur.asp']")[0].text
        if debug: self.log.info(self.who,"vol_editor found")

        if soup.select("a[href*='collection.asp']"): vol_coll = soup.select("a[href*='collection.asp']")[0].text
        if debug: self.log.info(self.who,"vol_coll")

        for i in comment_generic.stripped_strings:
            tmp_lst.append(str(i))
        vol_coll_nbr = tmp_lst[len(tmp_lst)-1]
        if "n°" in vol_coll_nbr:
            for k in ["n°","(",")","-"]:
                if k in vol_coll_nbr:
                    vol_coll_nbr=vol_coll_nbr.replace(k,"")
            vol_coll_nbr = vol_coll_nbr.strip()
        else:
            vol_coll_nbr = ""
        if debug: self.log.info(self.who,"vol_coll_nbr found")

        for elemnt in soup.select("span[class='sousFicheNiourf']")[0].stripped_strings:
            if "Dépôt légal" in elemnt:
                elemnt = elemnt.replace("Dépôt légal :","").strip()
            if len(str(vol_dp_lgl))<3:
                if "trimestre" in elemnt:
                    ele=(elemnt.replace(","," ")).split()
                    vol_dp_lgl=datetime.datetime.strptime(("000"+str((int(ele[0][0])-1)*91+47))[-3:]+" "+ele[2],"%j %Y")
                for i in ("janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"):
                    if i in elemnt:
                        vol_dp_lgl=elemnt
                        vol_dp_lgl=datetime.datetime.strptime(vol_dp_lgl,"%B %Y")
                        break
            if "ISBN" in elemnt:
                vol_isbn = elemnt.lower().replace(" ","").replace('isbn:','')
                if "néant" in vol_isbn: vol_isbn=""
                if debug: self.log.info(self.who,"vol_isbn found")
            if "Genre" in elemnt: vol_genre = elemnt.lstrip("Genre : ")
        if debug: self.log.info(self.who,"vol_dp_lgl, vol_isbn, vol_genre found")

        if soup.select("img[name='couverture']"):
            for elemnt in repr(soup.select("img[name='couverture']")[0]).split('"'):
                if "http" in elemnt:
                    if not vol_cover_index:
                        vol_cover_index = elemnt
                        if debug: self.log.info(self.who,"vol_cover_index found")

        if vol_cover_index:
            comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">'+ vol_cover_index +'</a></p></div>',"lxml")

    # select the fields I want... More exist such as film adaptations or references to advises to read
    # but that is not quite consistant around all the books (noosfere is a common database from many people)
    # and beside I have enough info like that AND I do NOT want to take out the noosfere's business

        tmp_comm_lst=soup.select("td[class='onglet_biblio1']")
#        if debug: self.log.info(self.who,tmp_comm_lst)             #usefull but too long
        for i in range(len(tmp_comm_lst)):
            if "Quatrième de couverture" in str(tmp_comm_lst[i]):
                comment_pre_resume = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Quatrième de couverture</p></div>',"lxml")
                comment_resume = soup.select("div[id='Résumes']")[0]
                if debug: self.log.info(self.who,"comment_resume found")

            if "Critique" in str(tmp_comm_lst[i]):
                if not "autres" in str(tmp_comm_lst[i]):
                    comment_pre_Critique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques</p></div>',"lxml")
                    comment_Critique = soup.select("div[id='Critique']")[0]
                    if debug: self.log.info(self.who,"comment_Critique found")

            if "Sommaire" in str(tmp_comm_lst[i]):
                comment_pre_Sommaire = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Sommaire</p></div>',"lxml")
                comment_Sommaire = soup.select("div[id='Sommaire']")[0]
                if debug: self.log.info(self.who,"comment_Sommaire found")

            if "Critiques des autres" in str(tmp_comm_lst[i]):
                comment_pre_AutresCritique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques des autres éditions ou de la série</p></div>',"lxml")
                comment_AutresCritique = soup.select("div[id='AutresCritique']")[0]
                if debug: self.log.info(self.who,"comment_AutresCritique found")
                if comment_AutresCritique.select('a[href*="serie.asp"]'):
                    if not comment_AutresCritique.select('a[href*="serie.asp"]')[0].find_parents("div", {'id':'critique'}):
                        critic_url = "https://www.noosfere.org/livres/"+comment_AutresCritique.select('a[href*="serie.asp"]')[0]['href']
                        try:
                            comment_AutresCritique=self.get_Critique_de_la_serie(critic_url)
                        except:
                            self.log.exception("get_Critique_de_la_serie failed for url: ",critic_url)


    # group in a big bundle all the fields I think I need

        if comment_cover:
            vol_comment_soup.append(comment_cover)
        if comment_generic:
            vol_comment_soup.append(comment_generic)
        if comment_resume:
            vol_comment_soup.append(comment_pre_resume)
            vol_comment_soup.append(comment_resume)
        if comment_Critique:
            vol_comment_soup.append(comment_pre_Critique)
            vol_comment_soup.append(comment_Critique)
        if comment_Sommaire:
            vol_comment_soup.append(comment_pre_Sommaire)
            vol_comment_soup.append(comment_Sommaire)
        if comment_AutresCritique:
            vol_comment_soup.append(comment_pre_AutresCritique)
            vol_comment_soup.append(comment_AutresCritique)
        if comment_decoupage_annexe:
            vol_comment_soup.append(comment_pre_decoupage_annexe)
            vol_comment_soup.append(comment_decoupage_annexe)

    #
    # Make a minimum of "repair" over vol_comment_soup so that it displays correctly in the comments and in my catalogs
    # - I hate justify when it makes margin "float" around the correct position (in fact when space are used instead of absolute positioning)
    # - I like to have functional url when they exist
    # - I like to find out the next and/or previous books in a serie

        for elemnt in vol_comment_soup.select('[align="justify"]'):
            del elemnt['align']

    # remove all double or triple 'br' to improve presentation.
    # Note: tmp1 and tmp2 must contain a different value from any possible first elemnt. (yes, I am lrp and I am unique :-) )
    #
    # ouais, et alors, si je modifie comment_generic APRES l'avoir integré à vol_comment_soup, il n'y a qu'une seule version en mémoire...
    # donc vol_comment_soup est modifié...
    #

        tmp1=tmp2="lrp_the_unique"
        for elemnt in comment_generic.findAll():
            tmp1,tmp2=tmp2,elemnt
            if tmp1==tmp2:
                elemnt.extract()

        for elemnt in vol_comment_soup.select("a[href*='auteur.asp']"):
            elemnt["href"]=elemnt["href"].replace("/livres/auteur.asp","https://www.noosfere.org/livres/auteur.asp")
        for elemnt in vol_comment_soup.select("a[href*='serie.asp']"):
            elemnt["href"]=elemnt["href"].replace("serie.asp","https://www.noosfere.org/livres/serie.asp")
        for elemnt in vol_comment_soup.select("a[href*='EditionsLivre.asp']"):
            elemnt["href"]=elemnt["href"].replace("./EditionsLivre.asp","https://www.noosfere.org/livres/EditionsLivre.asp")
        for elemnt in vol_comment_soup.select("a[href*='editionslivre.asp']"):
            elemnt["href"]=elemnt["href"].replace("editionslivre.asp","https://www.noosfere.org/livres/editionslivre.asp")
        for elemnt in vol_comment_soup.select("a[href*='editeur.asp']"):
            elemnt["href"]=elemnt["href"].replace("editeur.asp","https://www.noosfere.org/livres/editeur.asp")
        for elemnt in vol_comment_soup.select("a[href*='editeur.asp']"):
            elemnt["href"]=elemnt["href"].replace("collection.asp","https://www.noosfere.org/livres/collection.asp")

        fg,fd="<==","==>" #chr(0x21D0),chr(0x21D2)   #chr(0x27f8),chr(0x27f9)
        if vol_comment_soup.select_one("img[src*='arrow_left']"): vol_comment_soup.select_one("img[src*='arrow_left']").replace_with(fg)
        if vol_comment_soup.select_one("img[src*='arrow_right']"): vol_comment_soup.select_one("img[src*='arrow_right']").replace_with(fd)

    # ok, all collected, make it fit typewise for mi cache cover and set mi

        if vol_serie:
            if vol_serie_seq.isnumeric(): vol_serie_seq = float(vol_serie_seq)
            else: vol_serie_seq = 1.0
        vol_comment_soup = vol_comment_soup.encode('ascii','xmlcharrefreplace')

        self.log.info(self.who,"+++"*25)
        self.log.info(self.who,"lrpid, type()                  : ",self.lrpid, type(self.lrpid))                    # must be <class 'str'>
        self.log.info(self.who,"relevance, type()              : ",self.relevance, type(self.relevance))            # must be <class 'float'>
        self.log.info(self.who,"vol_title, type()              : ",vol_title, type(vol_title))                      # must be <class 'str'>
        self.log.info(self.who,"vol_auteur, type()             : ",vol_auteur, type(vol_auteur))                    # must be <class 'list'> of <class 'str'>
        self.log.info(self.who,"vol_auteur_prenom, type()      : ",vol_auteur_prenom, type(vol_auteur_prenom))      # must be <class 'str'>
        self.log.info(self.who,"vol_auteur_nom, type()         : ",vol_auteur_nom, type(vol_auteur_nom))            # must be <class 'str'>
        if vol_serie:
            self.log.info(self.who,"vol_serie, type()              : ",vol_serie, type(vol_serie))                  # must be <class 'str'>
            self.log.info(self.who,"vol_serie_seq, type()          : ",vol_serie_seq, type(vol_serie_seq))          # must be <class 'float'>
        self.log.info(self.who,"vol_editor, type()             : ",vol_editor, type(vol_editor))                    # must be <class 'str'>
        self.log.info(self.who,"vol_coll, type()               : ",vol_coll, type(vol_coll))                        # must be
        self.log.info(self.who,"vol_coll_nbr, type()           : ",vol_coll_nbr, type(vol_coll_nbr))                # must be
        self.log.info(self.who,"vol_dp_lgl, type()             : ",vol_dp_lgl, type(vol_dp_lgl))                    # must be <class 'datetime.datetime'> ('renderer=isoformat')
        self.log.info(self.who,"vol_isbn, type()               : ",vol_isbn, type(vol_isbn))                        # must be <class 'str'>
        self.log.info(self.who,"vol_genre, type()              : ",vol_genre, type(vol_genre))                      # must be <class 'list'> of <class 'str'>
        self.log.info(self.who,"vol_cover_index, type()        : ",vol_cover_index, type(vol_cover_index))          # must be
        self.log.info(self.who,"type(vol_comment_soup)         : ",type(vol_comment_soup))                          # must be byte encoded (start with b'blablabla...
#        self.log.info(self.who,"vol_comment_soup               :\n",vol_comment_soup)                                # Maybe a bit long sometimes
                                                                                                               # language must be <class 'str'>

        if vol_isbn and vol_cover_index:
            self.plugin.cache_identifier_to_cover_url(self.lrpid, vol_cover_index)

        if vol_isbn:
            self.plugin.cache_isbn_to_identifier(vol_isbn, self.lrpid)


        mi = Metadata(vol_title, [vol_auteur])
        mi.set_identifier('lrpid', self.lrpid)
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
        
        # UTF-8 characters may be serialized different ways, only xmlcharrefreplace produces xml compatible strings
        # any other non ascii character with another utf-8 byte representation will make calibre behave with the messsage:
        # ValueError: All strings must be XML compatible: Unicode or ASCII, no NULL bytes or control characters
        # Side note:
        # I have no real good url structure(html 3 times, div a sibling of html...), but calibre does not seems to care (nice :-) )
        #
        # Ca m'a pris un temps fou pour trouver, par hazard (enfin, quasi par hazard, j' ai essayé tout ce qui pouvait ameliorer
        # la compatibilité avec xml... mais je lisais mal et je pensais à une incompatibilité avec la structure xml),
        # que encode('ascii','xmlcharrefreplace') aidait bien...
        #
        mi.comments = vol_comment_soup

        if debug: self.log.info(self.who,"mi\n",mi,"\n")
        self.plugin.clean_downloaded_metadata(mi)

        self.result_queue.put(mi)

##
##    def _get_metadata(self, book_id, get_user_categories=True):  # {{{
##        mi = Metadata(None, template_cache=self.formatter_template_cache)
##
##        mi._proxy_metadata = ProxyMetadata(self, book_id, formatter=mi.formatter)
##
##        author_ids = self._field_ids_for('authors', book_id)
##        adata = self._author_data(author_ids)
##        aut_list = [adata[i] for i in author_ids]
##        aum = []
##        aus = {}
##        aul = {}
##        for rec in aut_list:
##            aut = rec['name']
##            aum.append(aut)
##            aus[aut] = rec['sort']
##            aul[aut] = rec['link']
##        mi.title       = self._field_for('title', book_id,
##                default_value=_('Unknown'))
##        mi.authors     = aum
##        mi.author_sort = self._field_for('author_sort', book_id,
##                default_value=_('Unknown'))
##        mi.author_sort_map = aus
##        mi.author_link_map = aul
##        mi.comments    = self._field_for('comments', book_id)
##        mi.publisher   = self._field_for('publisher', book_id)
##        n = utcnow()
##        mi.timestamp   = self._field_for('timestamp', book_id, default_value=n)
##        mi.pubdate     = self._field_for('pubdate', book_id, default_value=n)
##        mi.uuid        = self._field_for('uuid', book_id,
##                default_value='dummy')
##        mi.title_sort  = self._field_for('sort', book_id,
##                default_value=_('Unknown'))
##        mi.last_modified = self._field_for('last_modified', book_id,
##                default_value=n)
##        formats = self._field_for('formats', book_id)
##        mi.format_metadata = {}
##        mi.languages = list(self._field_for('languages', book_id))
##        if not formats:
##            good_formats = None
##        else:
##            mi.format_metadata = FormatMetadata(self, book_id, formats)
##            good_formats = FormatsList(sorted(formats), mi.format_metadata)
##        # These three attributes are returned by the db2 get_metadata(),
##        # however, we dont actually use them anywhere other than templates, so
##        # they have been removed, to avoid unnecessary overhead. The templates
##        # all use _proxy_metadata.
##        # mi.book_size   = self._field_for('size', book_id, default_value=0)
##        # mi.ondevice_col = self._field_for('ondevice', book_id, default_value='')
##        # mi.db_approx_formats = formats
##        mi.formats = good_formats
##        mi.has_cover = _('Yes') if self._field_for('cover', book_id,
##                default_value=False) else ''
##        mi.tags = list(self._field_for('tags', book_id, default_value=()))
##        mi.series = self._field_for('series', book_id)
##        if mi.series:
##            mi.series_index = self._field_for('series_index', book_id,
##                    default_value=1.0)
##        mi.rating = self._field_for('rating', book_id)
##        mi.set_identifiers(self._field_for('identifiers', book_id,
##            default_value={}))
##        mi.application_id = book_id
##        mi.id = book_id
##        composites = []
##        for key, meta in self.field_metadata.custom_iteritems():
##            mi.set_user_metadata(key, meta)
##            if meta['datatype'] == 'composite':
##                composites.append(key)
##            else:
##                val = self._field_for(key, book_id)
##                if isinstance(val, tuple):
##                    val = list(val)
##                extra = self._field_for(key+'_index', book_id)
##                mi.set(key, val=val, extra=extra)
##        for key in composites:
##            mi.set(key, val=self._composite_for(key, book_id, mi))
##
##        user_cat_vals = {}
##        if get_user_categories:
##            user_cats = self.backend.prefs['user_categories']
##            for ucat in user_cats:
##                res = []
##                for name,cat,ign in user_cats[ucat]:
##                    v = mi.get(cat, None)
##                    if isinstance(v, list):
##                        if name in v:
##                            res.append([name,cat])
##                    elif name == v:
##                        res.append([name,cat])
##                user_cat_vals[ucat] = res
##        mi.user_categories = user_cat_vals
##
##        return mi
##    # }}}
