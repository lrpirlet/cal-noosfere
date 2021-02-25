#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2021, Louis Richard Pirlet'
__docformat__ = 'restructuredtext en'

from bs4 import BeautifulSoup as BS
import socket, re, datetime
from threading import Thread

from lxml.html import fromstring, tostring

from calibre.ebooks.metadata.book.base import Metadata
from calibre.ebooks.metadata import check_isbn
from calibre.library.comments import sanitize_comments_html
from calibre.utils.cleantext import clean_ascii_chars
from calibre.utils.icu import lower

class Worker(Thread):
    # Get volume details, in a separate thread, from noosfere vol page from (book_url)s found in __init__


    def __init__(self, log, book_url, lrpid, book_title, isbn, result_queue, browser, relevance, plugin, timeout=20):

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
        self.cover_url = None
        self.who="[worker "+str(relevance)+"]"
        self.from_encoding="windows-1252"

        if debug:
            self.log.info("\nEntering worker", relevance)
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
        #
        debug=1
        if debug: self.log.info(self.who,"Entering run(self)")

        wrk_url = self.book_url
        if debug: self.log.info(self.who,"wrk_url : ",wrk_url)
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
        if debug:
            self.log.info(self.who,"\nIn verify_isbn(isbn_str)")
            self.log.info(self.who,"isbn_str         : ",isbn_str)

        for k in ['(',')','-',' ']:
            if k in isbn_str:
                isbn_str=isbn_str.replace(k,"")
        if debug:
            self.log.info(self.who,"isbn_str cleaned : ",isbn_str)
            self.log.info(self.who,"return from verify_isbn\n")

        return check_isbn(isbn_str)         # calibre does the check for me after cleaning...

    def ret_top_vol_indx(self, url, book_title):
        # cette fonction reçoit la soupe de l'url du livre qui contient plusieur volumes du meme auteur, dont certains ont le meme ISBN et generalement
        # le meme titres.
        #
        # selection aleatoire??? non
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
        if debug:
            self.log.info(self.who,"\nIn ret_top_vol_indx(self, url, title)")
            self.log.info(self.who,"url        : ",url)
            self.log.info(self.log,"book_title : ",book_title)

        sr=self.br.open(url,timeout=20)
        soup = BS(sr, "html.parser",from_encoding=self.from_encoding)

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
                self.log.info(self.log,"vol_isbn : ",vol_isbn)
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

            ts_vol_index[str(int(count/2))]=(point,vol_index,vol_editor)


            if debug:
                self.log.info(self.who,"key                   : ",str(int(count/2)))
                self.log.info(self.who,"vol_index             : ",vol_index)
                self.log.info(self.who,"vol_title             : ",vol_title)
                self.log.info(self.who,"vol_cover_index       : ",vol_cover_index)
                self.log.info(self.who,"vol_editor            : ",vol_editor)
                self.log.info(self.who,"vol_isbn              : ",vol_isbn)
                self.log.info(self.who,"vol_collection        : ",vol_collection)
                self.log.info(self.who,"point                 : ",point)
                self.log.info(self.who,"======================")
                self.log.info(self.who,"\nfound",int(count/2+1),"volumes différents")

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

    def get_Critique_de_la_serie(self, critic_url):
        # La critique de la serie peut etre developpée dans une autre page dont seul l(url est d'interet
        # cette fondtion remplce le pointeur par le contenu.
        #
        # The critic for a serie may be set appart in another page. The vol url refers to that other loacation.
        # I want to have it local to my volume.
        #
        debug=1
        if debug: self.log.info(self.who,"\nIn get_Critique_de_la_serie(self, critic_url)")

        sr=self.br.open(critic_url,timeout=20)
        soup = BS(sr, "html.parser",from_encoding=self.from_encoding)
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
        if debug:
            self.log.info(self.who,"\nIn extract_vol_details(soup)")
            self.log.info(self.who,"vol_url       : ",vol_url)

        sr=self.br.open(vol_url,timeout=20)
        url_vrai=sr.geturl()
        if debug:
            self.log.info(self.who,"sr.info()     :\n", sr.info())
            self.log.info(self.who,"ha ouais, vraiment? charset=iso-8859-1... c'est pas vrai, c'est du", self.from_encoding,"...")
            self.log.info(self.who,"# isolé pour trouver quel est l'encodage d'origine... ça marchait à peu pres sans forcer encodage d'entrée mais pas tout a fait")
            self.log.info(self.who,"# il n'est pas improbable que ce soit ça que le site va modifier dans le futur...")
            self.log.info(self.who,"#")
            self.log.info(self.who,'# variable "from_encoding" isolated to find out what is the site character encoding... The announced charset is WRONG')
            self.log.info(self.who,"# requests was able to decode correctly, I knew that my setup was wrong but it took me a while...")
            self.log.info(self.who,"# Maybe I should have tried earlier the working solution as the emitting node is MS")
            self.log.info(self.who,"# (Thanks MS!!! and I mean it as I am running W10.. :-) but hell, proprietary standard is not standard)...")
            self.log.info(self.who,"# It decode correctly to utf_8 with windows-1252 forced as from_encoding")
            self.log.info(self.who,"# watch-out noosfere is talking about making the site better... ;-}")
            self.log.info(self.who,"#'")
            self.log.info(self.who,"sr.getcode()  : ",sr.getcode())
            self.log.info(self.who,"url_vrai      : ",url_vrai)

        soup = BS(sr, "html.parser",from_encoding=self.from_encoding)
#        if debug: self.log.info(self.who,soup.prettify())              # useful but too big...

        tmp_lst=[]
        vol_info={}
        vol_title=vol_auteur=vol_auteur_prenom=vol_auteur_nom=vol_serie=vol_serie_seq=vol_editor=vol_coll=vol_coll_nbr=vol_dp_lgl=vol_isbn=vol_genre=vol_cover_index=""
        comment_generic=comment_resume=comment_Critique=comment_Sommaire=comment_AutresCritique=comment_cover=None

        vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"html.parser")
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
        vol_auteur_prenom = vol_auteur_prenom.strip()
        if debug: self.log.info(self.who,"vol_auteur_prenom found")
        vol_auteur_nom = vol_auteur_nom.strip()
        if debug: self.log.info(self.who,"vol_auteur_nom found")

        if soup.select("a[href*='serie.asp']"):
            vol_serie = soup.select("a[href*='serie.asp']")[0].text
            tmp_vss = [x for x in soup.select("a[href*='serie.asp']")[0].parent.stripped_strings]
            for i in range(len(tmp_vss)):
                if "vol." in tmp_vss[i]:
                    vol_serie_seq=tmp_vss[i].replace("vol.","").strip()
        if debug: self.log.info(self.who,"vol_cycle, vol_serie_seq found")

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
                vol_dp_lgl = elemnt.replace("Dépôt légal :","").strip()
            if len(str(vol_dp_lgl))<3:
                for i in ("trimestre","janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"):
                    if i in elemnt:
                        vol_dp_lgl=elemnt
                        break
            if "ISBN" in elemnt:
                vol_isbn = elemnt.lower().replace(" ","")
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
            comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">Link to image </a></p></div>',"html.parser")

    # select the fields I want... More exist such as film adaptations or references to advises to read
    # but that is not quite consistant around all the books (noosfere is a common database from many people)
    # and beside I have enough info like that AND I do NOT want to take out the noosfere's business

        tmp_comm_lst=soup.select("td[class='onglet_biblio1']")
#        if debug: self.log.info(self.who,tmp_comm_lst)             #usefull but too long
        for i in range(len(tmp_comm_lst)):
            if "Quatrième de couverture" in str(tmp_comm_lst[i]):
                comment_pre_resume = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Quatrième de couverture</p></div>',"html.parser")
                comment_resume = soup.select("div[id='Résumes']")[0]
                if debug: self.log.info(self.who,"comment_resume found")

            if "Critique" in str(tmp_comm_lst[i]):
                if not "autres" in str(tmp_comm_lst[i]):
                    comment_pre_Critique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques</p></div>',"html.parser")
                    comment_Critique = soup.select("div[id='Critique']")[0]
                    if debug: self.log.info(self.who,"comment_Critique found")

            if "Sommaire" in str(tmp_comm_lst[i]):
                comment_pre_Sommaire = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Sommaire</p></div>',"html.parser")
                comment_Sommaire = soup.select("div[id='Sommaire']")[0]
                if debug: self.log.info(self.who,"comment_Sommaire found")

            if "Critiques des autres" in str(tmp_comm_lst[i]):
                comment_pre_AutresCritique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques des autres éditions ou de la série</p></div>',"html.parser")
                comment_AutresCritique = soup.select("div[id='AutresCritique']")[0]
                if debug: self.log.info(self.who,"comment_AutresCritique found")
                if comment_AutresCritique.select('a[href*="serie.asp"]'):
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

        if debug:
            self.log.info(self.who,"vol_title              : ",vol_title)
            self.log.info(self.who,"vol_auteur             : ",vol_auteur)
            self.log.info(self.who,"vol_auteur_prenom      : ",vol_auteur_prenom)
            self.log.info(self.who,"vol_auteur_nom         : ",vol_auteur_nom)
            self.log.info(self.who,"vol_serie              : ",vol_serie)
            self.log.info(self.who,"vol_serie_seq          : ",vol_serie_seq)
            self.log.info(self.who,"vol_editor             : ",vol_editor)
            self.log.info(self.who,"vol_coll               : ",vol_coll)
            self.log.info(self.who,"vol_coll_nbr           : ",vol_coll_nbr)
            self.log.info(self.who,"vol_dp_lgl             : ",vol_dp_lgl)
            self.log.info(self.who,"vol_isbn               : ",vol_isbn)
            self.log.info(self.who,"vol_genre              : ",vol_genre)
            self.log.info(self.who,"vol_cover_index        : ",vol_cover_index)
            self.log.info(self.who,"vol_comment_soup       :\n",vol_comment_soup)          # Maybe a bit long sometimes
            self.log.info(self.who,"=======================")

        vol_comment_soup = sanitize_comments_html(vol_comment_soup.encode())
        if debug:
            self.log.info(self.who,"vol_comment_soup       :\n",vol_comment_soup)          # Maybe a bit long sometimes


            
