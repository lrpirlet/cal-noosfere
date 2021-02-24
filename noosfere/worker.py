#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2014, David Forrester <davidfor@internode.on.net>'
__docformat__ = 'restructuredtext en'

import socket, re, datetime
from threading import Thread

from lxml.html import fromstring, tostring

from calibre.ebooks.metadata.book.base import Metadata
from calibre.library.comments import sanitize_comments_html
from calibre.utils.cleantext import clean_ascii_chars
from calibre.utils.icu import lower

from calibre_plugins.noosfere import noosfere

class Worker(Thread): 
    # Get volume details, in a separate thread, from noosfere vol page from (book_url)s found in __init__

    def __init__(self, log, url, lrpid, result_queue, browser, relevance, plugin, timeout=20):

        debug=1

        Thread.__init__(self)
        self.daemon = True
        self.log = log
        self.url = url
        self.lrpid = lrpid
        self.result_queue = result_queue
        self.browser = browser.clone_browser()
        self.relevance = relevance
        self.plugin = plugin
        self.timeout = timeout
        self.cover_url = self.isbn = None

        if debug:
            log.info("\nEntering worker", relevance)
            log.info("self                  : ", self)
            log.info("log                   : ", log)
            log.info("url                   : ", url)
            log.info("lrpid                 : ", lrpid)
            log.info("result_queue          : ", result_queue)
            log.info("browser, self.browser : ", browser, self.browser)
            log.info("relevance             : ", relevance)
            log.info("plugin                : ", plugin)
            log.info("timeout               : ", timeout)
        
    def run(self):

        sys.exit("ici on stoppe")
    
        try:
            self.get_details()
        except:
            self.log.exception('get_details failed for url: %r'%self.url)


##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##
##    for key,ref in book_index.items():
##        livrel,indexl = key,ref
##        if debug: print("livrel : ",livrel,"indexl : ",indexl)
##
##rqt = indexl+"&Tri=3"
##ret_rqt = req_mtd_get(rqt)
##soup,url_vrai = ret_rqt[0],ret_rqt[1]
##if debug:
##    print("soup = req_mtd_get(rqt)",soup.prettify())
##    print("url_vrai : ",url_vrai)
##
##if "numitem" in url_vrai:           #url_vrai contient .../livres/editionsLivre.asp?numitem=69&Tri=3 si plusieurs volumes du livre
##    if debug: print("allez, ecore un effort, faut trouver le bon volume")
##    top_vol_indx = ret_top_vol_indx(soup,livrel)   #vol_indx est un pointeur vers le livre
##    if debug: print(top_vol_indx)
##    rqt = (top_vol_indx+"&Tri=3").replace("./niourf","/livres/niourf")
##    ret_rqt = req_mtd_get(rqt)
##    soup,url_vrai = ret_rqt[0],ret_rqt[1]
##    if debug:
##        print("soup = req_mtd_get(rqt)",soup.prettify())
##        print("url_vrai : ",url_vrai)
##
##elif "numlivre" in url_vrai:    #url_vrai contient ...livres/niourf.asp?numlivre=7479 si le livre est trouvé
##    if debug: print("livre  trouvé")
##else:
##    print("quelquechose ne va pas, bug???")
##
##vol_info=extr_vol_details(soup)  # we get vol_info from the book
##if debug: print("vol_info: ",vol_info)
##
##
##******************************************************************************
def ret_top_vol_indx(soup,livrel):
    # cette fonction recoit une page qui contient plusieur volume de meme auteur, dont certains ont le meme ISBN et generalement
    # le meme titres.
    #
    # selection aleatoire???
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
    if debug: print("\n in ret_top_vol_indx(soup,livrel)")

    ts_vol_index={}

    nbr_of_vol=soup.select("td[class='item_bib']")
    for count in range(0,len(nbr_of_vol),2):
        subsoup=nbr_of_vol[count]
        point=0
        vol_index=vol_title=vol_cover_index=vol_editor=vol_isbn=vol_collection=""

        if subsoup.select("a[href*='numlivre']"): vol_index=subsoup.select("a[href*='numlivre']")[0]['href']

        if subsoup.select("a > img"): vol_title=subsoup.select("a > img")[0]['alt']
        if livrel.title()==vol_title.title():
            point+=1

        if subsoup.select("a > img"):
            vol_cover_index=subsoup.select("a > img")[0]['src']
            point+=1

        if subsoup.select("a[href*='numediteur']"): vol_editor=subsoup.select("a[href*='numediteur']")[0].text

        if subsoup.select("span[class='SousFicheNiourf']"):
            vol_isbn = verify_isbn(subsoup.select("span[class='SousFicheNiourf']")[0].text).lower().strip()
            if vol_isbn:
                point+=500
                if verify_isbn(lrplivre)== vol_isbn: point+=1000

        if subsoup.select("a[href*='collection']"): vol_collection=subsoup.select("a[href*='collection']")[0].text

        if subsoup.select("img[src*='3dbullgreen']"):
            point+=2

        tmp_presence=subsoup.select("span[title*='Présence']")
        for i in range(len(tmp_presence)):
            if "R" in tmp_presence[i].text: point+=1
            elif "C" in tmp_presence[i].text: point+=1
            elif "CS" in tmp_presence[i].text: point+=1
            elif "S" in tmp_presence[i].text: point+=1

    # lrp Ce choix constitue un racourci qui devrait etre remplacé par une presentation à l'utilisateur pour qu'il choisisse

        ts_vol_index[str(int(count/2))]=(point,vol_index,vol_editor)


        if debug:
            print("key                   : ",str(int(count/2)))
            print("vol_index             : ",vol_index)
            print("vol_title             : ",vol_title)
            print("vol_cover_index       : ",vol_cover_index)
            print("vol_editor            : ",vol_editor)
            print("vol_isbn              : ",vol_isbn)
            print("vol_collection        : ",vol_collection)
            print("point                 : ",point)
            print("======================")
            print("\nfound",int(count/2+1),"volumes différents")

    top_vol_point,top_vol_index,serie_editeur=0,"",[]

    for key,ref in ts_vol_index.items():
        serie_editeur.append(ts_vol_index[key][2])

    top_vol_editor={}.fromkeys(set(serie_editeur),0)

    for editr in serie_editeur:
        top_vol_editor[editr]+=1

    for key,ref in ts_vol_index.items():
        if debug: print("La clé est", key,"la valeur des points est", ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]],"le pointeur est",ts_vol_index[key][1],"l'éditeur est",ts_vol_index[key][2])
        if ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]>top_vol_point:
            top_vol_point=ts_vol_index[key][0]*top_vol_editor[ts_vol_index[key][2]]
            top_vol_index=ts_vol_index[key][1]

    return top_vol_index

def get_Critique_de_la_serie(rqt):
    # La critique de la serie peut etre developpée dans une autre page dont seul l(url est d'interet
    # cette fondtion remplce le pointeur par le contenu.
    #
    # The critic for a serie may be set appart in another page. The vol url refers to that other loacation.
    # I want to have it local to my volume.
    #
    debug=1
    if debug: print("\n in get_Critique_de_la_serie(rqt)")

    ret_rqt = req_mtd_get(rqt)
    soup = ret_rqt[0]
    if debug: print("""soup.select_one('div[id="SerieCritique"]')""",soup.select_one('div[id="SerieCritique"]'))

    return soup.select_one('div[id="SerieCritique"]')

def extr_vol_details(soup):
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
    if debug: print("\n in extr_vol_details(soup)")

    tmp_lst=[]
    vol_info={}
    vol_title=vol_auteur=vol_auteur_prenom=vol_auteur_nom=vol_serie=vol_serie_seq=vol_editor=vol_coll=vol_coll_nbr=vol_dp_lgl=vol_isbn=vol_genre=vol_cover_index=""
    vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"html.parser")
    comment_generic=comment_resume=comment_Critique=comment_Sommaire=comment_AutresCritique=comment_cover=None

    if debug: print(soup.prettify())

    if soup.select("span[class='TitreNiourf']"): vol_title = soup.select("span[class='TitreNiourf']")[0].text.strip()
    if debug: print("vol_title")

    if soup.select("span[class='AuteurNiourf']"): vol_auteur = soup.select("span[class='AuteurNiourf']")[0].text.replace("\n","").strip()
    if debug: print("vol_auteur")
    for i in range(len(vol_auteur.split())):
        if not vol_auteur.split()[i].isupper():
            vol_auteur_prenom += " "+vol_auteur.split()[i]
        else:
            vol_auteur_nom += " "+vol_auteur.split()[i].title()
    vol_auteur_prenom = vol_auteur_prenom.strip()
    if debug: print("vol_auteur_prenom")
    vol_auteur_nom = vol_auteur_nom.strip()
    if debug: print("vol_auteur_nom")

    if soup.select("a[href*='serie.asp']"):
        vol_serie = soup.select("a[href*='serie.asp']")[0].text
        tmp_vss = [x for x in soup.select("a[href*='serie.asp']")[0].parent.stripped_strings]
        for i in range(len(tmp_vss)):
            if "vol." in tmp_vss[i]:
                vol_serie_seq=tmp_vss[i].replace("vol.","").strip()
    if debug: print("vol_cycle, vol_serie_seq")

    comment_generic = soup.select("span[class='ficheNiourf']")[0]
    new_div=soup.new_tag('div')
    comment_generic = comment_generic.wrap(new_div)
    if debug: print("comment_generic")

    if soup.select("a[href*='editeur.asp']"): vol_editor = soup.select("a[href*='editeur.asp']")[0].text
    if debug: print("vol_editor")

    if soup.select("a[href*='collection.asp']"): vol_coll = soup.select("a[href*='collection.asp']")[0].text
    if debug: print("vol_coll")

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
    if debug: print("vol_coll_nbr")

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
            if debug: print("vol_isbn")
        if "Genre" in elemnt: vol_genre = elemnt.lstrip("Genre : ")
    if debug: print("vol_dp_lgl, vol_isbn, vol_genre")

    if soup.select("img[name='couverture']"):
        for elemnt in repr(soup.select("img[name='couverture']")[0]).split('"'):
            if "http" in elemnt:
                if not vol_cover_index:
                    vol_cover_index = elemnt
                    if debug: print("vol_cover_index")

    if vol_cover_index:
        comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">Link to image </a></p></div>',"html.parser")

# select the fields I want... More exist such as film adaptations or references to advises to read
# but that is not quite consistant around all the books (noosfere is a common database from many poeple)
# and beside I do NOT want to take out the noosfere's business

    tmp_comm_lst=soup.select("td[class='onglet_biblio1']")
    if debug: print(tmp_comm_lst)
    for i in range(len(tmp_comm_lst)):
        if "Quatrième de couverture" in str(tmp_comm_lst[i]):
            comment_pre_resume = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Quatrième de couverture</p></div>',"html.parser")
            comment_resume = soup.select("div[id='Résumes']")[0]
            if debug: print("comment_resume")

        if "Critique" in str(tmp_comm_lst[i]):
            if not "autres" in str(tmp_comm_lst[i]):
                comment_pre_Critique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques</p></div>',"html.parser")
                comment_Critique = soup.select("div[id='Critique']")[0]
                if debug: print("comment_Critique")

        if "Sommaire" in str(tmp_comm_lst[i]):
            comment_pre_Sommaire = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Sommaire</p></div>',"html.parser")
            comment_Sommaire = soup.select("div[id='Sommaire']")[0]
            if debug: print("comment_Sommaire")

        if "Critiques des autres" in str(tmp_comm_lst[i]):
            comment_pre_AutresCritique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques des autres éditions ou de la série</p></div>',"html.parser")
            comment_AutresCritique = soup.select("div[id='AutresCritique']")[0]
            if debug: print("comment_AutresCritique",comment_AutresCritique.prettify())
            if comment_AutresCritique.select('a[href*="serie.asp"]'):
                #if "Critique de la série" in comment_AutresCritique.select('a[href*="serie.asp"]')[0].text:
                comment_AutresCritique=get_Critique_de_la_serie("/livres/"+comment_AutresCritique.select('a[href*="serie.asp"]')[0]['href'])

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
                    

    vol_info["vol_auteur_prenom"]=vol_auteur_prenom
    vol_info["vol_auteur_nom"]=vol_auteur_nom
    vol_info["vol_title"]=vol_title
    vol_info["vol_serie"]=vol_serie
    vol_info["vol_serie_seq"]=vol_serie_seq
    vol_info["vol_editor"]=vol_editor
    vol_info["vol_coll"]=vol_coll
    vol_info["vol_coll_nbr"]=vol_coll_nbr
    vol_info["vol_dp_lgl"]=vol_dp_lgl
    vol_info["vol_isbn"]=vol_isbn
    vol_info["vol_genre"]=vol_genre
    vol_info["vol_cover_index"]=vol_cover_index
    vol_info["vol_comment_soup"]=vol_comment_soup

    if debug:
        print("vol_title              : ",vol_title)
        print("vol_auteur             : ",vol_auteur)
        print("vol_auteur_prenom      : ",vol_auteur_prenom)
        print("vol_auteur_nom         : ",vol_auteur_nom)
        print("vol_serie              : ",vol_serie)
        print("vol_serie_seq          : ",vol_serie_seq)
        print("vol_editor             : ",vol_editor)
        print("vol_coll               : ",vol_coll)
        print("vol_coll_nbr           : ",vol_coll_nbr)
        print("vol_dp_lgl             : ",vol_dp_lgl)
        print("vol_isbn               : ",vol_isbn)
        print("vol_genre              : ",vol_genre)
        print("vol_cover_index        : ",vol_cover_index)
        print("vol_comment_soup       :\n",vol_comment_soup)
        print("=======================")
        print("vol_info               : ",vol_info)

    return vol_info



##******************************************************************************
##    def get_details(self):
##        try:
##            self.log.info('KoboBooks url: %r'%self.url)
##            raw = self.browser.open_novisit(self.url, timeout=self.timeout).read().strip()
##        except Exception as e:
##            if callable(getattr(e, 'getcode', None)) and \
##                    e.getcode() == 404:
##                self.log.error('URL malformed: %r'%self.url)
##                return
##            attr = getattr(e, 'args', [None])
##            attr = attr if attr else [None]
##            if isinstance(attr[0], socket.timeout):
##                msg = 'Kobo Books timed out. Try again later.'
##                self.log.error(msg)
##            else:
##                msg = 'Failed to make details query: %r'%self.url
##                self.log.exception(msg)
##            return
##
##        raw = raw.decode('utf-8', errors='replace')
###         open('E:\\t3.html', 'wb').write(raw)
##
##        if '<title>404 - ' in raw:
##            self.log.error('URL malformed: %r'%self.url)
##            return
##
##        try:
##            root = fromstring(clean_ascii_chars(raw))
##        except:
##            msg = 'Failed to parse Kobo Books details page: %r'%self.url
##            self.log.exception(msg)
##            return
##
##        self.parse_details(root)
##
##    def parse_details(self, root):
##        try:
##            kobobooks_id = self.parse_kobobooks_id(self.url)
##            self.log('parse_details - kobobooks_id: "%s" ' % (kobobooks_id))
##        except:
##            self.log.exception('Error parsing URL for Kobo Books: %r'%self.url)
##            kobobooks_id = None
##
##        try:
##            title = self.parse_title(root)
##        except:
##            self.log.exception('Error parsing page for title: url=%r'%self.url)
##            title = None
##
##        try:
##            self.log('parse_details - root: ',tostring(root))
##            authors = self.parse_authors(root)
##        except:
##            self.log.exception('Error parsing page for authors: url=%r'%self.url)
##            authors = []
##
##        if not title or not authors or not kobobooks_id:
##            self.log.error('Could not find title/authors/KoboBooks id for %r'%self.url)
##            self.log.error('Kobo Books: %r Title: %r Authors: %r'%(kobobooks_id, title,
##                authors))
##            return
##
##        mi = Metadata(title, authors)
##        mi.set_identifier('kobo', kobobooks_id)
##        self.kobobooks_id = kobobooks_id
##
##        # Some of the metadata is in a JSON object in script tag.
##        try:
##            import json
##            scripts = root.xpath('//div[@data-kobo-widget="RatingAndReviewWidget"]/script')
##            if len(scripts) > 0:
##                json_details = scripts[1].text
##                if json_details is not None:
##                    page_metadata = json.loads(json_details, strict=False)
##                    self.log("Script page_metadata=", page_metadata)
##                    self.log("Script page_metadata keys=", page_metadata.keys())
##                    try:
##                        pubdate = page_metadata["releasedate"]
##                        pubdate = datetime.datetime.strptime(pubdate, "%Y-%m-%dT%H:%M:%S")
##                        mi.pubdate = pubdate
##                        self.log("pubdate from JSON:", mi.pubdate)
##                    except:
##                        self.log.exception('Error parsing page for pubdate: url=%r'%self.url)
##            
##                    try:
##                        mi.publisher = page_metadata["brand"]
##                    except:
##                        self.log.exception('Error parsing page for publisher: url=%r'%self.url)
##            
##                    try:
##                        isbn = page_metadata["gtin13"]
##                        if isbn:
##                            self.isbn = mi.isbn = isbn
##                    except:
##                        self.log.exception('Error parsing ISBN for url: %r'%self.url)
##            
##            else:
##                self.log("No scripts founds for book details metadata????")
##        except Exception as e:
##            self.log("Exception thrown getting scripts:", e)
##            
##
##        try:
##            (mi.series, mi.series_index) = self.parse_series(root)
##        except:
##            self.log.exception('Error parsing series for url: %r'%self.url)
##
##        try:
##            mi.tags = self.parse_tags(root)
##        except:
##            self.log.exception('Error parsing tags for url: %r'%self.url)
##
##        try:
##            mi.rating = self.parse_rating(root)
##        except:
##            self.log.exception('Error parsing ratings for url: %r'%self.url)
##
##        try:
##            self.cover_url = self.parse_cover(root)
##        except:
##            self.log.exception('Error parsing cover for url: %r'%self.url)
##        mi.has_cover = bool(self.cover_url)
##
##        try:
##            mi.comments = self.parse_comments(root)
##        except:
##            self.log.exception('Error parsing comments for url: %r'%self.url)
##
##        try:
##            language = self.parse_language(root)
##            if language:
##                self.lang = mi.language = language
##        except:
##            self.log.exception('Error parsing languages for url: %r'%self.url)
##
##        mi.source_relevance = self.relevance
##
##        if self.kobobooks_id:
##            if self.cover_url:
##                self.plugin.cache_identifier_to_cover_url(self.kobobooks_id, self.cover_url)
##
##        self.plugin.clean_downloaded_metadata(mi)
##
##        self.result_queue.put(mi)
##
##    def parse_kobobooks_id(self, url):
##        return re.search(KoboBooks.STORE_DOMAIN + KoboBooks.BOOK_PATH + '(.*)', url).groups(0)[0]
###        return re.search('store.kobobooks.com/en-US/ebook/(.*)', url).groups(0)[0]
##
##    def parse_title(self, root):
##        title_node = root.xpath('//h1/span[@class="title product-field"]')
##        if title_node:
##            return title_node[0].text.strip()
##
##    def parse_series(self, root):
##        series_node = root.xpath('//span[@class="series product-field"]/span[@class="product-sequence-field"]')
##        if series_node and len(series_node) > 0:
##            series_node = series_node[0]
##            self.log('parse_series - series_node: "%s" ' % (tostring(series_node)))
##            self.log('parse_series - series_node.text: "%s" ' % (series_node.text))
##            series_node = series_node.xpath('./a')[0]
##            self.log('parse_series - series_node: "%s" ' % (tostring(series_node)))
##            self.log('parse_series - series_node.text: "%s" ' % (series_node.text))
##            series_text = series_node.text
##            self.log('parse_series - series_name: "%s" ' % (series_name))
##            self.log("parse_series - series_index: ", series_node.xpath('./span[@class="book-number"]'))
##            try:
##                series_name, series_index = series_text.split('#')
##                series_index = int(series_index)
##            except:
##                series_name = series_text
##                series_index = None
##            series_name = series_name.strip()
##            self.log("parse_series - series_name=%s, series_index=%s" % (series_name, series_index))
##            return (series_name, series_index)
##        self.log('parse_series - no series info')
##        return (None, None)
##
##    def parse_authors(self, root):
##        self.log('parse_authors - root: "%s"' % root)
##        author = ','.join(root.xpath('//a[@class="contributor-name"]/text()'))
##        author = author.strip()
##        self.log('parse_authors - author: "%s"' % author)
##        author = author.split('by ')[-1]
##        authors = [a.strip() for a in author.split(',')]
##        self.log('parse_authors - authors: "%s"' % authors)
##
##        def ismatch(authors):
##            authors = lower(' '.join(authors))
##            amatch = not self.match_authors
##            for a in self.match_authors:
##                if lower(a) in authors:
##                    amatch = F
##                    break
##            if not self.match_authors: amatch = True
##            return amatch
##
##        if author == '' or not self.match_authors or ismatch(authors):
##            self.log('parse_authors - authors:', authors)
##            return authors
##        self.log('Rejecting authors as not a close match: ', ','.join(authors))
##
##    def parse_comments(self, root):
##        # The comments seem to have two slightly different containing divs.
##        description_node = root.xpath('//div[@class="synopsis-description-all"]')
##        self.log('parse_comments - description_node: "%s" ' % (description_node))
##        self.log('parse_comments - len(description_node): "%s" ' % (len(description_node)))
##        if len(description_node):
##            self.log('parse_comments - tostring(description_node[0]): "%s" ' % (tostring(description_node[0])))
##        try:
##            description_node = description_node[0]
##        except:
##            description_node = root.xpath('//div[@class="synopsis-description"]')
##            try:
##                description_node = description_node[0]
##            except:
##                description_node = None
##            
##        if description_node is not None:
##            comments = tostring(description_node, method='html')
##            comments = sanitize_comments_html(comments)
##            return comments
##        self.log('parse_comments - no comments found.')
##
##    def parse_rating(self, root):
##        rating_node = root.xpath('//div[@class="rating-review-summary-header"]/section[@class="overall-rating-container"]/@data-rating-value')
##        if rating_node:
##            try:
##                rating_text = rating_node[0]
##                rating_value = float(rating_text)
##                self.log('parse_rating - rating: "%s"' % rating_text)
##                return rating_value
##            except:
##                self.log('parse_rating - rating: "%s"' % "None")
##                return None
##
##    def parse_cover(self, root):
##        # Kobo have a higher resolution covers that get downloaded directly to the device. The images
##        # can be retrieved by setting the size of the cover. Kobo will send a cover that fits in this size
##        # and respects the aspect ratio of the stored cover.
##        # For example, the cover node is:
##        #    //kbimages1-a.akamaihd.net/019f9050-d9a5-4a4f-9720-e4abcdea627b/353/569/90/False/turn-coat.jpg
##        # In this, the image is 353x569.
##        # For the size, use the "maximum_cover_size" tweak. if this is not set, use 1650x2200. This is the detault for
##        # the tweak at the time writing.
##        from calibre.utils.config_base import tweaks
##        nwidth, nheight = tweaks['maximum_cover_size']
##        cover_node = root.xpath('//div[@class="main-product-image"]//img[contains(@class,"cover-image")]/@src')[0]
##        cover_node_text = "%s %s" %('http:', cover_node)
##        cover_node_split = cover_node_text.split('/')
##        cover_width_upsized = int(cover_node_split[4]) * 4
##        cover_height_upsized = int(cover_node_split[5]) * 4
##        cover_node_split[4] = str(nwidth)
##        cover_node_split[5] = str(nheight)
##        cover_node = '/'.join(cover_node_split).replace(' ', '')
##
###        if cover_node:
###            match = re.match('popupimg\(\'(.*)\'\)', cover_node[0])
###            if match:
###                return KoboBooks.BASE_URL + KoboBooks.BOOK_PATH + match.groups(0)[0]
###                return 'http://store.kobobooks.com/en-US/ebook/' + match.groups(0)[0]
##
##        return cover_node
##
##    def parse_language(self, root):
##        lang_node = root.xpath('//div[@class="bookitem-secondary-metadata"]/ul/li')[3]
##        if lang_node.text.strip() == 'Language:':
##            language = lang_node.xpath('./span')[0].text
##            self.log('parse_language - language: "%s" ' % (language))
##            return language
##
##    def parse_tags(self, root):
##        ans = []
##        # There are no exclusions at this point.
##        exclude_tokens = {}
##        exclude = {}
##        seen = set()
##        category_node = root.xpath('//ul[@class="category-rankings"]')
##        self.log('parse_tags - category_node: "%s" ' % (category_node))
##        self.log('parse_tags - len(category_node): "%s" ' % (len(category_node)))
##        self.log('parse_tags - tostring(category_node[0]): "%s" ' % (tostring(category_node[0])))
##        if len(category_node) > 0:
##            for li in category_node[0].xpath('./li'):
##                self.log('parse_tags - li: "%s" ' % (li))
##                self.log('parse_tags - len(li): "%s" ' % (len(li)))
##                self.log('parse_tags - tostring(li[0]): "%s" ' % (tostring(li[0])))
##                tag = ''
##                for i, a in enumerate(li.iterdescendants('a')):
##                    self.log('parse_tags - a: "%s" ' % (a))
##                    self.log('parse_tags - len(a): "%s" ' % (len(a)))
##                    if len(a) > 0:
##                        self.log('parse_tags - tostring(a[0]): "%s" ' % (tostring(a[0])))
##                    if self.category_handling == 'top_level_only' and i > 0:
##                        self.log('parse_tags - top level only and sub level category')
##                        continue
##                    raw = (a.text or '').strip().replace(',', ';')
##                    if self.category_handling == 'hierarchy' and i > 0:
##                        tag = tag + "." + raw
##                    else:
##                        tag = raw
##                    ltag = icu_lower(tag)
##                    tokens = frozenset(ltag.split())
##                    if tag and ltag not in exclude and not tokens.intersection(exclude_tokens) and ltag not in seen:
##                        ans.append(tag)
##                        seen.add(ltag)
##        return ans

