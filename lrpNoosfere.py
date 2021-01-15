import urllib
import urllib.request
import urllib.error
from bs4 import BeautifulSoup as BS
import sys

debug=1

lrpauteur = input("auteur : ")
if not len(lrpauteur):
    lrpauteur="vanvogt"     #n'existe pas
    lrpauteur="eschbach"   #2 existent
    lrpauteur="eschbach a*"   #1 existent
    lrpauteur="van vogt"   #1 existe

# noosfere accepts * to complete the name or the surname, trips on the dot in van vogt A.E.
lrpauteur=str(lrpauteur.replace(","," "))
lrpauteur=str(lrpauteur.replace(".","* "))

lrplivre = input("ISBN ou titre du livre) : ")
if not len(lrplivre):
    lrplivre = "cataplute "      # pas de livres
    lrplivre = "fondation"      # un tas de livres
    lrplivre = "2864243806"  #ISBN
    lrplivre = "kwest"          # un livre

    lrplivre = "2-277-12381-1"

print("lrpauteur : ",lrpauteur)
print("lrplivre : ",lrplivre)

base_url="https://www.noosfere.org"
search_urn=base_url+"/livres/noosearch.asp"
base_rkt={"ModeMoteur":"MOTSCLEFS","ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}

def req_mtd_post(rkt):
    # acces en mode post sur <base_url>/livres/noosearch.asp
    debug=0
    if debug: print("\nfuncion req_mtd_post(rkt)")

    rkt.update(base_rkt)
    req=urllib.parse.urlencode(rkt).encode('ascii')
    try: sr=urllib.request.urlopen(search_urn,req,timeout=15)
    except urllib.error.URLError as e:
        print("Une erreur enoyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    except timeout:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("rkt: ",rkt)
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = BS(sr, "html.parser")
    if debug: print(soup.prettify())
    return soup

def req_mtd_get(rqt):
    # acces en mode post sur <base_url>/livres/auteur.asp?numauteur=366
    debug=0
    if debug: print("\nfunction req_mtd_get(rqt)")

    url=base_url+rqt
    if debug: print("url : ",url)
    try: sr=urllib.request.urlopen(url,timeout=15)
    except urllib.error.URLError as e:
        print("Une erreur envoyée par le site a été reçue.")
        print("code : ",e.code,"reason : ",e.reason)
        sys.exit("réponse d'erreur de l'url, désolé")
    except timeout:
        print("A network timeout occurred, do you have wide world web access?")
        sys.exit("désolé")
    if debug:
        print("\ntype(sr) : ",type(sr))
        print("sr.info() : ",sr.info())
        print("sr.geturl() : ",sr.geturl())
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = BS(sr, "html.parser")
    if debug: print(soup.prettify())
    return (soup,sr.geturl())

def ret_autr_indx(soup):
    # Trouve la reference de l'auteur dans la soupe produite par noosfere
    # retourne auteur_index, un dictionnaire avec key=AUTEUR, val=href
    # L'idée est de renvoyer UNE seule reference... trouver l'auteur est primordial
    debug=0
    if debug: print("function ret_autr_indx(soup)")

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
    if debug: print("\nIn funtion ret_livr_ISBN_indx()")

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
    debug=0
    if debug: print("ret_livre_par_auteur_indx()")

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

def ret_top_vol_indx(soup):
    # cette fonction recoit une page qui contient plusieur volume de meme auteur, de meme ISBN et generalement de meme titres.
    # Ces volumes diffèrent par l'editeur, la date d'edition ou de réédition, l'image de couverture, le 4me de couverture, la critique.
    # MON choix se base sur un systeme de points:
    # isbn présent:                         3pt
    # résumé présent:                       2pt
    # critique présente:                    2pt
    # sommaire des nouvelles presentes:     2pt
    # titre different                      -1pt
    # plus tard, je pense construire une image + carateristique dans un bouton
    debug=1
    if debug: print("ret_top_vol_indx")

    top_vol_index={}
    item=[]
    for child in soup.recursiveChildGenerator():
        if child.name=="td" and "class" in child.attrs:
            if 'item_bib' in child["class"]:
                if debug:
                    print("\nfound 'result'")
                    #print("child (=subsoup) :\n",child.prettify())
                    #print("child",child.prettify())
                item.append(child)
                if debug: print(item)
    return item
    try:
        for child in subsoup.recursiveChildGenerator():
            if child.name=="a" and "href" in child.attrs:
                if debug:
                    print("child.text : ",child.text)
                    print("child['href'] : ",child['href'])
                livre_par_auteur_index[child.text]=(child["href"])
    except: print("Désolé, il semble que la DB ne connaisse aucun livre de cet auteur",auteura.title(),".\nOu qu'il y a un bug... :-)")
    
    return top_vol_index    
    

#ISBN (ou titre de livre)
# On émet une recherche avec vers noosfere avec isbn (ou titre de livre!)
# On reçoit, en principe, UNE reponse qui pointe vers soit le livre,
# soit une serie de livres réedités, ou édité chez plusieurs editeurs ou une combinaison des deux
# Quand le livre est trouve le url reel contient niourf.asp?numlivre=
# Quand le isbn (ou le titre) pointe vers plusieurs livres, une operation supplementaire est a faire

if debug:
    print("trouve ref pour : ",lrplivre)
rkt = {"Mots": lrplivre,"livres":"livres"}
soup = req_mtd_post(rkt)
livre_index = ret_livr_ISBN_indx(soup)
if len(livre_index) > 1:
    print("Désolé, trop de livres trouvés, veuillez entrer un des suivants : ")
    for key in livre_index:
        print(key.title())
if len(livre_index) == 0:
    print("Aucun livre trouvé, verifiez l'entrée : ",lrplivre,end=". ")
    sys.exit("Désolé.")
for key,ref in livre_index.items():
    livrel,indexl = key,ref
    if debug :
        print("livrel.title() : ",livrel.title(),"indexl : ",indexl)
rqt = indexl+"&Tri=3"
if debug: print("rqt ajoutée à base_url",rqt)
ret_rqt = req_mtd_get(rqt)
soup,url_vrai = ret_rqt[0],ret_rqt[1]
if debug:
    print("soup = req_mtd_get(rqt)",soup.prettify())
    print("url_vrai : ",url_vrai)
if "numitem" in url_vrai:       #url_vrai contient .../livres/editionsLivre.asp?numitem=69&Tri=3 si plusieurs editions du livre
    if debug: print("allez, ecore un effort, faut trouver le bon livre")
    top_vol_indx = ret_top_vol_indx(soup)   #vol_indx est un pointeur vers le livre
    # pour le moment top_vol_indx est en fait item, une liste de subsoup
#elif "numlivre" in url_vrai:    #url_vrai contient ...livres/niourf.asp?numlivre=7479 si le livre est trouvé
#    if debug: print("livre  trouvé")
else:
    print("quelquechose ne va pas, bug???")

    #return vol_idx    # si ceci est une fontion..
#print(top_vol_indx)

    
# explose top_vol_indx en auteur,isbn,titre,serie et N°de serie,editeur,collection d'editeur et N° de collection d'editeur,
# traducteur, graphiste et commentaire.
# Ce dernier contient la reference de nooSFere, le 4me de couverture (resumé), la ou les critique(s), sommaire (si recueil de nouvelles)


"""
#auteur
if debug:
    print("trouve ref pour : ",lrpauteur)
rkt = {"Mots":lrpauteur,"auteurs":"auteurs"}
soup = req_mtd_post(rkt)
auteur_index = ret_autr_indx(soup)               # quel est l'indexe de l'auteur? auteur is a dictionary
if len(auteur_index) == 0: sys.exit("Désolé, aucun auteur trouvé avec le nom : ",lrpauteur)
if len(auteur_index) > 1:
    print("Désolé, trop d'auteurs trouvés, veuillez entrer un des suivants : ")
    for key in auteur_index:
        print(key.title())
for key,ref in auteur_index.items():
    auteura,indexa = key,ref
    if debug :
        print("auteura.title() : ",auteura.title(),"indexa : ",indexa)
"""
"""
#livres attribués à un auteur connu
if debug: print("\nTrouve ref pour les livres de : ",lrpauteur," connu comme : ",auteura.title(),".")
rqt=indexa+"&Niveau=livres"
if debug: print("rqt ajoutée à base_url",rqt)
soup = req_mtd_get(rqt)
if debug: print("soup = req_mtd_get(rqt)",soup.prettify())
livre_par_auteur_index = ret_livr_par_auteur_indx(soup)
for key,ref in livre_par_auteur_index.items():
    livrelpa,indexlpa = key,ref
    if debug :
        print("livrelpa.title() : ",livrelpa.title(),"indexlpa : ",indexlpa)
"""    



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
