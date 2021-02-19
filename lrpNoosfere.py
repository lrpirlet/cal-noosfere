# Note: If this work (done to learn both python and the Hyper Text Markup Language) finds its way to the public domain, so be it.
# I have no problem with, and reserve the right to ignore, any error, choice and poor optimization.
# I use it, it is MY problem... You use it, it is YOUR problem
# For example, my mother language is French and my variable's names are MY choise for MY easy use...
# Anyway, I'll comment my in english or french or both depending when I write it (no comment please)

#import urllib
import urllib.request
import urllib.error
from bs4 import BeautifulSoup as BS
import sys


def make_soup(sr):
    # isolé pour trouver quel est l'encodage d'origine... ça marchait à peu pres sans forcer encodage d'entrée mais pas tout a fait
    # il n'est pas improbable que ce soit ça que le site va modifier dans le futur...
    #
    # function isolated to find out what is the site character encoding... The announced standard (in meta) is WRONG
    # requests was able to decode correctly, I knew that my setup was wrong but it took me a while...
    # Maybe I should have tried earlier the working solution as the emitting node is MS
    # (Thanks MS!!! and I mean it as I am running W10.. :-) but hell, proprietary standard is not standard)...
    # It decode correctly to utf_8 with windows-1252 is forced as input encoding
    # watch-out noosfere is talking about making the site better... ;-}
    #
    debug=0
    if debug: print("\n in make_soup(sr)")

    soup = BS(sr, "html.parser",from_encoding="windows-1252")
    if debug: print(soup.prettify())

    return soup

def verify_isbn(isbn_str):
    # isbn_str est brute d'extraction... la fonction renvoie un isbn correct ou "invalide"
    # Notez qu'on doit supprimr les characteres de separation et les characteres restants apres extraction
    # et que l'on traite un mot de 10 ou 13 characteres.
    #
    # ISBN10 a une longueur de 9 caracteres numerique plus 1 charactere de controle numerique ou "X" considéré
    # comme la representation de la valeur 10.
    # On calcule la validité de l'ISBN10 par l'equation suivante:
    # (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
    #
    # ISBN13 a une longueur de 12 charateres numeriques plus 1 charactere de controle numerique.
    # On calcule la validité de l'ISBN13 par l'équation suivante:
    # ((x1+x3+x5+X7+X9+X11+x13)+(3*(X2+X4+X6+X8+X10+X12))) % 10 == 0
    #
    # isbn_str is strait from extraction... function returns an ISBN maybe correct ...or not
    # Characters irrelevant to ISBN and separators inside ISBN must be removed,
    # the resulting word must be either 10 or 13 characters long.
    #
    # ISBN10 must be 9 digits long plus one control character this is either a digit or "X" representing numeric value 10
    # The ISBN10 is valid if the following equation is verified.
    # (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
    #
    # ISBN13 must be 12 digits long plus 1 control digit.
    # The validy of the l'ISBN13 is verified when this equation verify
    # ((x1+x3+x5+X7+X9+X11+x13)+(3*(X2+X4+X6+X8+X10+X12))) % 10 == 0
    #
    debug=0
    if debug: print("\n in verify_isbn(isbn_str)")

    total=0

    for k in ['(',')','-']:
        if k in isbn_str:
            isbn_str=isbn_str.replace(k,"")
    if not (len(isbn_str)==10 or len(isbn_str)==13):
        return "invalide"

    #ISBN10
    if len(isbn_str)==10:
        for i, m in enumerate(reversed(range(1, 11))):
            char = isbn_str[i]
            if char.isdigit():
                total = total + (10 * m)
            elif char.isalpha() and char == 'X' and i == 9:
                total = total + (10 * m)
            else:
                return ""
        if not (total % 11):
            return isbn_str


    # ISBN13
    else:
        for i in range(len(isbn_str)):           # Attention, les impairs sont d'index pair :) -- carefull here, the odd positions have an even index...
            if not isbn_str[i].isdigit():
                return "invalide"
            if i % 2:
                total+=(int(isbn_str[i])*3)
            else:
                total+=int(isbn_str[i])
        if not (total % 10):
            return isbn_str
        else:
            return ""

def req_mtd_post(rkt,ModeMoteur="LITTERAL"):
    # Accède en mode post sur <base_url>/livres/noosearch.asp
    # Access using "post" method over <base_url>/livres/noosearch.asp
    #
    debug=1
    if debug: print("\nin req_mtd_post(rkt)")

    search_urn="https://www.noosfere.org/livres/noosearch.asp"
    base_rkt={"ModeMoteur":ModeMoteur,"ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}

    rkt.update(base_rkt)
    if debug: print("rkt",rkt)
    req=urllib.parse.urlencode(rkt).encode('ascii')
    try: sr=urllib.request.urlopen(search_urn,req,timeout=30)
    except TimeoutError:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    except urllib.error.HTTPError as e:
        print("Une erreur enovyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    except urllib.error.URLError as e:
        print("Une erreur enovyée par le site a été reçue.")
        print("reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("rkt: ",rkt)
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = make_soup(sr)
    return soup

def req_mtd_get(rqt):
    # Accède <base_url>/livres/auteur.asp?numauteur=366 en mode get, renvoie la soup et le vrai url utilisé.
    # Access <base_url>/livres/auteur.asp?numauteur=366 using get mode, send back soup and the real url used
    #
    debug=0
    if debug: print("\n in req_mtd_get(rqt)")

    url="https://www.noosfere.org"+rqt
    if debug: print("url : ",url)
    try: sr=urllib.request.urlopen(url,timeout=30)
    except TimeoutError:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    except urllib.error.HTTPError as e:
        print("Une erreur enovyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    except urllib.error.URLError as e:
        print("Une erreur enovyée par le site a été reçue.")
        print("reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("sr.info() : ",sr.info())
        print("sr.geturl() : ",sr.geturl())
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = make_soup(sr)

    return (soup,sr.geturl())

def ret_author_index(soup):
    # Trouve la reference de l'auteur dans la soupe de noosfere
    # retourne author_index, un dictionnaire avec key=AUTEUR, val=href
    # L'idée est de renvoyer UNE seule reference... trouver l'auteur est primordial si isbn is indisponible
    #
    # Find author references in the soup produced by noosfere, return author_index a dictionary with key=author, val=href
    # the idea is to find ONE single reference... to get the author is important is isbn is unavailable
    #
    debug=1
    if debug: print("\n in ret_author_index(soup)")

    author_index={}

    tmp_ai=soup.select('a[href*="auteur.asp"]')
    if len(tmp_ai):
        for i in range(len(tmp_ai)):
            if debug:
                print("tmp_ai["+str(i)+"].text, tmp_ai["+str(i)+"]['href'] : ",tmp_ai[i].text,tmp_ai[i]["href"])
            author_index[tmp_ai[i].text]=(tmp_ai[i]["href"])

    return author_index

def ISBN_ret_book_index(soup):
    # Trouver la reference d'un livre (titre ou ISBN) dans la soupe produite par noosfere
    # retourne book_index{}, un dictionnaire avec key=titre (key=ISBN), val=href
    # L'idée est de trouver UNE seule reference... 
    # Attention: on retourne une reference qui peut contenir PLUSIEURs volumes
    # C'est a dire: différents editeurs, différentes re-éditions et/ou, meme, un titre different... YESss)
    #
    # Find the book's reference (either title or ISBN) in the returned soup from noosfere
    # returns book_index{}, a dictionnary with key=title (key=ISBN), val=href
    # The idea is to find ONE unique reference...
    # Caution: the reference may contains several volumes, 
    # each with potentialy a different editor, a different edition date,... and even a different title
    #
    debug=1
    if debug: print("\n in ISBN_ret_book_index(soup)")

    book_index={}

    tmp_rbi=soup.select('a[href*="editionsLivre.asp"]')
    if len(tmp_rbi):
        for i in range(len(tmp_rbi)):
            if debug:
                print("tmp_rbi["+str(i)+"].text, tmp_rbi["+str(i)+"]['href'] : ",tmp_rbi[i].text,tmp_rbi[i]["href"])
            book_index[tmp_rbi[i].text]=(tmp_rbi[i]["href"])

    return book_index

def ret_book_per_author_index(soup):
    # Find the books references of a known author from the returned soup for noosfere
    # returns a dict "book_per_author_index{}" with key as title and val as the link to the book
    # Idea is to send back a few references that hopefully contains the title expected
    #
    # Trouver la reference des livres d'un auteur connu dans la soupe produite par noosfere
    # retourne "book_per_author_index{}", un dictionnaire avec key=titre, val=href
    # L'idée est de renvoyer serie de reference, dont on extrait les livres proches de lrplivre
    #
    debug=1
    if debug: print("\n in ret_livre_par_auteur_indx(soup)")

    book_per_author_index={}

    tmp_bpai=soup.select('a[href*="EditionsLivre.asp"]')
    for i in range(len(tmp_bpai)):
        if debug:
            print("tmp_bpai["+str(i)+"].text, tmp_bpai["+str(i)+"]['href'] : ",tmp_bpai[i].text,tmp_bpai[i]["href"])
        book_per_author_index[tmp_bpai[i].text]=(tmp_bpai[i]["href"])
        
    return book_per_author_index

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
    # isbn present                          i   2pt
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
                point+=2
                if verify_isbn(lrplivre)== vol_isbn: point+=10000

        if subsoup.select("a[href*='collection']"): vol_collection=subsoup.select("a[href*='collection']")[0].text

        if subsoup.select("img[src*='3dbullgreen']"):
            point+=2

        tmp_presence=subsoup.select("span[title*='Présence']")
        for i in range(len(tmp_presence)):
            if "R" in tmp_presence[i].text: point+=1
            elif "C" in tmp_presence[i].text: point+=1
            elif "CS" in tmp_presence[i].text: point+=1
            elif "S" in tmp_presence[i].text: point+=1

    # lrp Ce choix constitue un racourci qui devrait etre remplacé par une presentation à l'utilisateur pour qu il choisisse

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


debug=0

##lrpauteur = input("auteur : ")
##if not len(lrpauteur):
##    lrpauteur="vanvogt"     #n'existe pas
##    lrpauteur="eschbach"   #2 existent
##    lrpauteur="eschbach a*"   #1 existent
##    lrpauteur="van vogt"   #1 existe
##
### noosfere accepts * to complete the name or the surname, trips on the dot in van vogt A.E.
##lrpauteur=str(lrpauteur.replace(","," "))
##lrpauteur=str(lrpauteur.replace(".","* "))

lrplivre = input("ISBN ou titre du livre) : ")
if not len(lrplivre):
    lrplivre = "cataplute "      # pas de livres
    lrplivre = "kwest"          # un livre
    lrplivre = "fondation"      # un tas de livres
    lrplivre = "Fondation Et Empire"      # un livre dans serie mais ca marche pas car noosfere groupe livres similaires
    lrplivre = "2-277-12381-1"  # a poursuite des slans
    lrplivre = "2864243806"  #ISBN mars blanche
    lrplivre = "2-277-11880-X"  #serie anthologie J sadoul
    lrplivre = "2-265-03148-8"
    lrplivre = "2266085360"

##print("lrpauteur : ",lrpauteur)
lrplivre = lrplivre.replace(","," ")
print("lrplivre : ",lrplivre)

#ISBN (ou titre de livre)
if debug: print("je suis a #ISBN (ou titre de livre)")
# On émet une recherche avec vers noosfere avec isbn (ou titre de livre!)
# On reçoit, en principe, UNE reponse qui pointe vers soit le livre,
# soit une serie de livres réedités, ou édité chez plusieurs editeurs ou une combinaison des deux
# Quand le livre est trouve le url reel contient niourf.asp?numlivre=
# Quand le isbn (ou le titre) pointe vers plusieurs livres, une operation supplementaire est a faire

if debug: print("trouve ref pour : ",lrplivre)

rkt = {"Mots": lrplivre,"livres":"livres"}
soup = req_mtd_post(rkt)
book_index = ISBN_ret_book_index(soup)
if not len(book_index):
    print("Aucun livre trouvé, verifiez l'entrée : ",lrplivre,end=". ")
    sys.exit("Désolé.")
elif len(book_index) > 1:
    for key,ref in book_index.items():
        livrel,indexl = key,ref
        print("livrel : ",livrel,"indexl : ",indexl)
        #sys.exit("Désolé, trop de livres trouvés, veuillez entrer un des précédants : ")
else:
    for key,ref in book_index.items():
        livrel,indexl = key,ref
        if debug: print("livrel : ",livrel,"indexl : ",indexl)

rqt = indexl+"&Tri=3"
ret_rqt = req_mtd_get(rqt)
soup,url_vrai = ret_rqt[0],ret_rqt[1]
if debug:
    print("soup = req_mtd_get(rqt)",soup.prettify())
    print("url_vrai : ",url_vrai)

if "numitem" in url_vrai:           #url_vrai contient .../livres/editionsLivre.asp?numitem=69&Tri=3 si plusieurs volumes du livre
    if debug: print("allez, ecore un effort, faut trouver le bon volume")
    top_vol_indx = ret_top_vol_indx(soup,livrel)   #vol_indx est un pointeur vers le livre
    if debug: print(top_vol_indx)
    rqt = (top_vol_indx+"&Tri=3").replace("./niourf","/livres/niourf")
    ret_rqt = req_mtd_get(rqt)
    soup,url_vrai = ret_rqt[0],ret_rqt[1]
    if debug:
        print("soup = req_mtd_get(rqt)",soup.prettify())
        print("url_vrai : ",url_vrai)

elif "numlivre" in url_vrai:    #url_vrai contient ...livres/niourf.asp?numlivre=7479 si le livre est trouvé
    if debug: print("livre  trouvé")
else:
    print("quelquechose ne va pas, bug???")

vol_info=extr_vol_details(soup)  # we get vol_info from the book
if debug: print("vol_info: ",vol_info)


sys.exit("on sort ici...")


#auteur

if debug:
    print("je suis a #auteur")
    print("trouve ref pour : ",lrpauteur)

rkt = {"Mots":lrpauteur,"auteurs":"auteurs"}
soup = req_mtd_post(rkt)
author_index = ret_author_index(soup)               # quel est l'indexe de l'auteur? auteur is a dictionary

if not len(author_index):
    sys.exit("Désolé, aucun auteur trouvé avec le nom : ",lrpauteur)  
if len(author_index) > 1:
    for key in author_index:
        print(key.title())
    print("Désolé, trop d'auteurs trouvés, veuillez entrer un des précédents : ")       
for key,ref in author_index.items():
    auteura,indexa = key,ref
    if debug: print("auteura.title() : ",auteura.title(),"indexa : ",indexa)


#livres attribués à un auteur connu

if debug:
    print("\nje suis a #livres attribués à un auteur connu")
    print("Trouve ref pour les livres de : ",lrpauteur," connu comme : ",auteura.title(),".")

rqt=indexa+"&Niveau=livres"
if debug: print("in rqt ajoutée à base_url",rqt)

ret_rqt = req_mtd_get(rqt)
soup,url_vrai_lpa = ret_rqt[0],ret_rqt[1]
if debug: print("soup = req_mtd_get(rqt)",soup.prettify())

book_per_author_index = ret_book_per_author_index(soup)
for key,ref in book_per_author_index.items():
    livrelpa,indexlpa = key,ref
    if debug: print("livrelpa.title() : ",livrelpa.title(),"indexlpa : ",indexlpa)





