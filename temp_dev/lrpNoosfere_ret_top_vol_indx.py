#import urllib
import urllib.request
import urllib.error
from bs4 import BeautifulSoup as BS
import sys

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

    debug=1
    if debug: print("\nverify_isbn(isbn_str)")

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
                return "invalide"
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
        if (total % 10)==0:
            return isbn_str
        else:
            return "invalide"

def make_soup(sr):
    # isolé pour trouver quel est l'encodage d'origine... ça marchait a peu pres pour utf_8 mais pas tout a fait
    # il n'est pas improbable que ce soit ca que le site va modifier dans le futur...

    debug=0
    if debug: print("\nin make_soup(sr)")

    soup = BS(sr, "html.parser",from_encoding="windows-1252")
    if debug: print(soup.prettify())

    return soup

def req_mtd_post(rkt):
    # acces en mode post sur <base_url>/livres/noosearch.asp -- access using "post" method over <base_url>/livres/noosearch.asp
    debug=0
    if debug: print("\nin req_mtd_post(rkt)")

    rkt.update(base_rkt)
    req=urllib.parse.urlencode(rkt).encode('ascii')
    try: sr=urllib.request.urlopen(search_urn,req,timeout=15)
    except TimeoutError:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    except urllib.error.URLError as e:
        print("Une erreur enovyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("rkt: ",rkt)
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = make_soup(sr)
    return soup

def req_mtd_get(rqt):
    # accede <base_url>/livres/auteur.asp?numauteur=366
    # renvoie la soup et le vrai url (a mettre en commentaires pour reference)
    debug=0
    if debug: print("\nin req_mtd_get(rqt)")

    url=base_url+rqt
    if debug: print("url : ",url)
    try: sr=urllib.request.urlopen(url,timeout=15)
    except TimeoutError:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    except urllib.error.URLError as e:
        print("Une erreur envoyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("sr.info() : ",sr.info())
        print("sr.geturl() : ",sr.geturl())
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = make_soup(sr)

    return (soup,sr.geturl())

def ret_autr_indx(soup):
    # Trouve la reference de l'auteur dans la soupe produite par noosfere
    # retourne auteur_index, un dictionnaire avec key=AUTEUR, val=href
    # L'idée est de renvoyer UNE seule reference... trouver l'auteur est primordial
    debug=1
    if debug: print("\nin ret_autr_indx(soup)")

    auteur_index={}
    for child in soup.recursiveChildGenerator():
        if child.name=="div" and "id" in child.attrs:
            if debug:
                print('div and "id" true?',child.name=="div" and "id" in child.attrs)
                print(child.attrs)
                print('"result" in child["id"] true?',"result" in child["id"])
            if "result" in child["id"]:
                if debug:
                    print("\nfound 'result'")
                    print("child (=subsoup) :\n",child.prettify())
                    print("child",child.prettify())
                subsoup=child
    try:
        for child in subsoup.recursiveChildGenerator():
            if child.name=="a" and "href" in child.attrs:
                if debug:
                    print("child.text : ",child.text)
                    print("child['href'] : ",child['href'])
                auteur_index[child.text]=(child["href"])
    except: print("Désolé, l'auteur",lrpauteur," n'a pas été trouvé.")
    if debug:
        print("auteur_index: ",auteur_index)
        print("len(auteur_index) :",len(auteur_index))
    return auteur_index

def ret_livr_ISBN_indx(soup):
    # Trouver la reference d'un livre (titre ou ISBN) dans la soupe produite par noosfere
    # retourne livre_index, un dictionnaire avec key=titre (key=ISBN), val=href
    # L'idée est de renvoyer UNE seule reference... parfait pour ISBN
    # Attention: on retourne une reference qui peut contenir PLUSIEURs editions
    # C'est a dire: différents editeurs, différentes re-éditions et/ou, meme, un titre different... YESss)
    debug=0
    if debug: print("\nin ret_livr_ISBN_indx()")

    livre_index={}
    for child in soup.recursiveChildGenerator():
        if child.name=="div" and "id" in child.attrs:
            if 'result' in child["id"]:
                if debug:
                    print("\nfound 'result'")
                    print("child (=subsoup) :\n",child.prettify())
                    print("child",child.prettify())
                subsoup=child
    try:
        for child in subsoup.recursiveChildGenerator():
            if child.name=="a" and "href" in child.attrs:
                if debug:
                    print("child.text : ",child.text)
                    print("child['href'] : ",child['href'])
                livre_index[child.text]=(child["href"])
    except: print("Désolé, le livre",lrplivre," n'a pas été trouvé.")
    if debug:
        print("livre_index: ",livre_index)
        print("len(livre_index) :",len(livre_index))
    return livre_index

def ret_livr_par_auteur_indx(soup):
    #Trouver la reference des livres d'un auteur connu dans la soupe produite par noosfere
    # retourne livre_par_auteur_index, un dictionnaire avec key=titre, val=href
    # L'idée est de renvoyer serie de reference, dont on extrait les livres proches de lrplivre
    debug=1
    if debug: print("\nin ret_livre_par_auteur_indx()")

    livre_par_auteur_index={}
    for child in soup.recursiveChildGenerator():
        if child.name=="div" and "id" in child.attrs:
            if 'BiblioRomans1' in child["id"]:
                if debug:
                    print("\nfound 'result'")
                    print("child (=subsoup) :\n",child.prettify())
                    print("child",child.prettify())
                subsoup=child
    try:
        for child in subsoup.recursiveChildGenerator():
            if child.name=="a" and "href" in child.attrs:
                if debug:
                    print("child.text : ",child.text)
                    print("child['href'] : ",child['href'])
                livre_par_auteur_index[child.text]=(child["href"])
    except: print("Désolé, il semble que la DB ne connaisse aucun livre de cet auteur",auteura.title(),".\nOu qu'il y a un bug... :-)")
    return livre_par_auteur_index


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
    if debug: print("\nin ret_top_vol_indx")
    print("this function needs to be rewritten")

    ts_vol_index={}
    count=0
    vol_index=vol_title=vol_cover_index=vol_editor=vol_isbn=vol_collection=""

    for child in soup.recursiveChildGenerator():
        if child.name=="td" and "class" in child.attrs and 'item_bib' in child["class"]:
            count+=1
            if not count%2 == 0:
                subsoup=child
                point=0
                for child in subsoup.recursiveChildGenerator():
                    # vol_index
                    if child.name == "a":
                        if "href" in child.attrs and "numlivre" in child["href"]:
                            vol_index=child["href"]
                        continue
                    # vol_title, t, vol_cover_index, p
                    if child.name=="img":
                        if ("alt" and "src" and "title") in child.attrs and "Cliquez" in child["title"]:
                            vol_title = child["alt"]
                            if livrel.title()==vol_title.title():
                                point+=1
                            if "http" in child["src"]:
                                vol_cover_index = child["src"]
                                point+=1
                        continue
                    # vol_editor, vol_isbn, i
                    if child.name=="a":
                        if "href" in child.attrs and "numediteur" in child["href"]:
                            vol_editor=child.text
                            # vol_isbn may be next
                            tmp=child.find_next("span")
                            vol_isbn = verify_isbn(tmp.text)
                            if not vol_isbn=="invalide":
                                point+=2
                                if verify_isbn(lrplivre)== vol_isbn:
                                    point+=10000
                        continue
                    # vol_collection
                    if child.name=="a":
                        if "href" in child.attrs and "collection" in child["href"]:
                            vol_collection = child.text
                        continue
                    # information verifiée -- verified information
                    if child.name=="img":
                        if ("src" and "title") in child.attrs:
                            if "3dbullgreen" in child["src"]:
                                point+=2
                        continue
                    if child.name=="span":
                        if ("class" and "name" and "title") in child.attrs and "Présence" in child["title"]:
                            if "R" in child.text: point+=1
                            elif "C" in child.text: point+=1
                            elif "CS" in child.text: point+=1
                            elif "S" in child.text: point+=1
                        continue
                    continue        # évite le code debug dans la boucle -- avoid having debug code in the loop

                # lrp Ceci constitue un racourci qui devrait etre remplacé par une presentation à l'utilisateur

                ts_vol_index[str(int(count/2))]=(point,vol_index,vol_editor)

                # lrp avec une possibilité de choix fonction de ce qu'il veut...

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
        print("\nfound",int((count-1)/2),"volumes différents")

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
    if debug: print("extr_vol_details(soup)")

    tmp1=tmp2="junk"
    tmp_lst=[]
    vol_info={}
    vol_title=vol_auteur=vol_auteur_prenom=vol_auteur_nom=vol_serie=vol_serie_seq=vol_editor=vol_coll=vol_coll_nbr=vol_dp_lgl=vol_isbn=vol_genre=vol_cover_index=""
    vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"html.parser")
    comment_generic=comment_resume=comment_Critique=comment_Sommaire=comment_AutresCritique=comment_cover=None

##    for child in soup.recursiveChildGenerator():
##        if child.name=="div" and "id" in child.attrs and "Fiche_livre" in child["id"]:
##            subsoup=child
    if debug: print(soup.prettify())

    vol_title = soup.select("span[class='TitreNiourf']")[0].text.strip()
    if debug: print("vol_title")

    vol_auteur = soup.select("span[class='AuteurNiourf']")[0].text.replace("\n","").strip()
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

    try:
        vol_serie = soup.select("a[href*='serie.asp']")[0].text
    except:
        vol_serie = ""
    if debug: print("vol_cycle")

    print("vol_serie_seq must be implemented!!!")

    comment_generic = soup.select("span[class='ficheNiourf']")[0]
    new_div=soup.new_tag('div')
    comment_generic = comment_generic.wrap(new_div)
    if debug: print("comment_generic")

    vol_editor = soup.select("a[href*='editeur.asp']")[0].text
    if debug: print("vol_editor")

    vol_coll = soup.select("a[href*='collection.asp']")[0].text
    if debug: print("vol_coll")

    for i in comment_generic.stripped_strings:
        tmp_lst.append(str(i))
    vol_coll_nbr = tmp_lst[len(tmp_lst)-1]
    if "n°" in vol_coll_nbr:
        vol_coll_nbr = vol_coll_nbr.replace("n°","").strip()
    else:
        vol_coll_nbr = ""
    
    if debug: print("vol_coll_nbr")

    for elemnt in soup.select("span[class='sousFicheNiourf']")[0].stripped_strings:
        if "Dépôt légal" in elemnt:
            vol_dp_lgl = elemnt.replace("Dépôt légal :","").strip()
            if debug: print("vol_dp_lgl")
        if len(str(vol_dp_lgl))<3:
            for i in ("trimestre","janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"):
                if i in elemnt:
                    vol_dp_lgl=elemnt
                    break
        if "ISBN" in elemnt:
            vol_isbn = elemnt
            if "néant" in vol_isbn: vol_isbn=""
            if debug: print("vol_isbn")
        if "Genre" in elemnt: vol_genre = elemnt.lstrip("Genre : ")

    for elemnt in repr(soup.select("img[name='couverture']")[0]).split('"'):
        if "http" in elemnt:
            if not vol_cover_index:
                vol_cover_index = elemnt
                if debug: print("vol_cover_index")

    if vol_cover_index:
        comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">Link to image </a></p></div>',"html.parser")

    tmp_comm_lst=soup.select("td[class='onglet_biblio1']")
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
            if debug: print("comment_AutresCritique")

#
# ici probleme si .append il semble disparaitre de subsoup.. (faut copier ailleur avant .append ou renvoyer le .append apres la find du bouclage...
# a partir d'ici on peut detruire soup et subsoup

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
# - I hate justify when it makes margin "float" around the correct position (in fact when space are used instead of tab)
# - I like to have functional url when they exist
#

    for elemnt in vol_comment_soup.select('[align="justify"]'):
        del elemnt['align']

    for child in vol_comment_soup.recursiveChildGenerator():
        if child.name=="a" and "href" in child.attrs and "auteur.asp" in child["href"]:
            child["href"]=child["href"].replace("/livres/auteur.asp","https://www.noosfere.org/livres/auteur.asp")
            if debug: print(child["href"])
        if child.name=="a" and "href" in child.attrs and "serie.asp" in child["href"]:
            child["href"]=child["href"].replace("serie.asp","https://www.noosfere.org/livres/serie.asp")
            if debug: print(child["href"])
        if child.name=="a" and "href" in child.attrs and "EditionsLivre.asp" in child["href"]:
            child["href"]=child["href"].replace("./EditionsLivre.asp","https://www.noosfere.org/livres/EditionsLivre.asp")
            if debug: print(child["href"])
        if child.name=="a" and "href" in child.attrs and "editionslivre.asp" in child["href"]:
            child["href"]=child["href"].replace("editionslivre.asp","https://www.noosfere.org/livres/editionslivre.asp")
            if debug: print(child["href"])
        if child.name=="a" and "href" in child.attrs and "editeur.asp" in child["href"]:
            child["href"]=child["href"].replace("editeur.asp","https://www.noosfere.org/livres/editeur.asp")
            if debug: print(child["href"])
        if child.name=="a" and "href" in child.attrs and "collection.asp" in child["href"]:
            child["href"]=child["href"].replace("collection.asp","https://www.noosfere.org/livres/collection.asp")
            if debug: print(child["href"])

# need to understand local resources and modify argum. 2 of .replace(1,2) to access it

        if child.name=="img" and "src" in child.attrs and "arrow_left" in child["src"]:
            child["src"]=child["src"].replace("/images/arrow_left.gif","/images/arrow_left.gif")
            if debug: print(child)
        if child.name=="img" and "src" in child.attrs and "arrow_right" in child["src"]:
            child["src"]=child["src"].replace("/images/arrow_right.gif","/images/arrow_right.gif")
            if debug: print(child)

### remove all double 'br' to improve presentation, note tmp1 and tmp2 must contain an value different from any first elemnt

        for elemnt in comment_generic.findAll():
            tmp1,tmp2=tmp2,elemnt
            if tmp1==tmp2:
                elemnt.extract()

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


debug=1

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
    lrplivre = "fondation"      # un tas de livres
    lrplivre = "2864243806"  #ISBN
    lrplivre = "kwest"          # un livre
    lrplivre = "2-277-12381-1"

##print("lrpauteur : ",lrpauteur)
print("lrplivre : ",lrplivre)

base_url="https://www.noosfere.org"
search_urn=base_url+"/livres/noosearch.asp"
base_rkt={"ModeMoteur":"MOTSCLEFS","ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}

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
livre_index = ret_livr_ISBN_indx(soup)
if not len(livre_index):
    print("Aucun livre trouvé, verifiez l'entrée : ",lrplivre,end=". ")
    sys.exit("Désolé.")
elif len(livre_index) > 1:
    print("Désolé, trop de livres trouvés, veuillez entrer un des suivants : ")
    for key in livre_index:
        print(key.title())
else:
    for key,ref in livre_index.items():
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

if "numlivre" in url_vrai:    #url_vrai contient ...livres/niourf.asp?numlivre=7479 si le livre est trouvé
    if debug: print("livre  trouvé")
else:
    print("quelquechose ne va pas, bug???")

vol_info=extr_vol_details(soup)  # we get vol_info from the book
if debug: print("vol_info: ",vol_info)

sys.exit("fin tekporaire")





#auteur

if debug:
    print("je suis a #auteur")
    print("trouve ref pour : ",lrpauteur)

rkt = {"Mots":lrpauteur,"auteurs":"auteurs"}
soup = req_mtd_post(rkt)
auteur_index = ret_autr_indx(soup)               # quel est l'indexe de l'auteur? auteur is a dictionary

if not len(auteur_index):
    sys.exit("Désolé, aucun auteur trouvé avec le nom : ",lrpauteur)
if len(auteur_index) > 1:
    print("Désolé, trop d'auteurs trouvés, veuillez entrer un des suivants : ")
    for key in auteur_index:
        print(key.title())
for key,ref in auteur_index.items():
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

livre_par_auteur_index = ret_livr_par_auteur_indx(soup)
for key,ref in livre_par_auteur_index.items():
    livrelpa,indexlpa = key,ref
    if debug: print("livrelpa.title() : ",livrelpa.title(),"indexlpa : ",indexlpa)




""" ok, mais faut finaliser #livres attribués à un auteur connu pour creer un dictionaire d'ouvrage

#livre et auteur connu
if debug:
    print("\nTrouve ref pour les publication de : ",livrel.title()," de : ",auteura.title(),".")
rqt="/livres/EditionsLivre.asp?"+indexl.split("?")[1]+"&"+indexa.split("?")[1]
soup = req_mtd_get(rqt)
"""

""" reference
import re
import requests

s = '<a class=gb1 href=[^>]+>'
r = requests.get('https://www.google.com/?q=python')
result = re.search(s, r.text)

print result.group(0)
If you simply need the list of all matches you can use: re.findall(s, r.text)

share  follow
"""

""" reference
lrpall = re.findall(r'(.?livres/auteur.*?)\n',sr.text)
#lrpall = re.search(r'(.?livres/auteur.*?)\n',sr.text)

if debug:
        print("lrpall : ",lrpall)

if not len(lrpall):  # use this test for findall
#if not lrpall:
        print("Auteur inconnu, verifier manuellement")
        import sys
        sys.exit("Auteur inconnu...")
else:
        if debug:
                for i in range(len(lrpall)):
                        print(lrpall[i])
        ret_autr_indx()

#ok, we have the author index, just get book requested
#lrplivre = input("titre du livre")
#if debug:
#        if not len(lrplivre):
#                lrplivre="kwest"
#requests
"""
