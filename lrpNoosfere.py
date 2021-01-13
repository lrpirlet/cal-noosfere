import urllib
import urllib.request
import urllib.error
from bs4 import BeautifulSoup as BS
import sys

debug=1

lrpauteur = input("auteur : ")
if not len(lrpauteur):
    lrpauteur="vanvogt"     #n'existe pas
    lrpauteur="van vogt"   #1 existe
    lrpauteur="eschbach"   #2 existent
    lrpauteur="eschbach a*"   #1 existent

# noosfere accepts * to complete the name or the surname, trips on the dot in van vogt A.E.
lrpauteur=str(lrpauteur.replace(","," "))
lrpauteur=str(lrpauteur.replace(".","* "))

lrplivre = input("titre du livre ou ISBN: ")
if not len(lrplivre):
    lrplivre = "cataplute "      # pas de livres
    lrplivre = "fondation"      # un tas de livres
    lrplivre = "2864243806"  #ISBN
    lrplivre = "kwest"          # un livre

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
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = BS(sr, "html.parser")
    if debug: print(soup.prettify())
    return soup

def ret_autr_indx(soup):
    # Trouve la reference de l'auteur dans la soupe produite par noosfere
    # retourne auteurindex, un dictionnaire avec key=AUTEUR, val=href
    debug=0
    if debug: print("function ret_autr_indx(soup)")

    auteurindex={}
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
                auteurindex[child.text]=(child["href"])
    except: print("Désolé, l'auteur",lrpauteur," n'a pas été trouvé.")

    if debug: print("auteurindex: ",auteurindex)
    if debug: print("len(auteurindex) :",len(auteurindex))

    if len(auteurindex) > 1:
        print("Désolé, trop d'auteurs trouvés, veuillez entrer un des suivants : ")
        for key in auteurindex:
            print(key.title())
    return auteurindex

def ret_livr_indx(soup):
    # Trouver la reference d'un livre (titre ou ISBN) dans la soupe produite par noosfere
    # retourne livreindex, un dictionnaire avec key=titre (key=ISBN), val=href
    debug=0
    if debug: print("\nIn funtion ret_livr_indx()")

    livreindex={}
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
                livreindex[child.text]=(child["href"])
    except: print("Désolé, le livre",lrplivre," n'a pas été trouvé.")

    if debug: print("livreindex: ",livreindex)
    if debug: print("len(livreindex) :",len(livreindex))

    if len(livreindex) > 1:
        print("Désolé, trop de livres trouvés, veuillez entrer un des suivants : ")
        for key in livreindex:
            print(key.title())
    return livreindex

def ret_isbn_indx():
    # essayons un acces en mode post sur noosearch_simple.asp pour trouver la reference d'un isbn
    # retourne livreindex, un dictionnaire avec key=titre, val=href
    debug=1
    if debug: print("ret_isbn_indx()")

#auteur
if debug:
    print("trouve ref pour : ",lrpauteur)
rkt = {"Mots":lrpauteur,"auteurs":"auteurs"}
soup = req_mtd_post(rkt)
auteurindex = ret_autr_indx(soup)               # quel est l'indexe de l'auteur? auteur is a dictionary
if len(auteurindex) != 1: sys.exit("Désolé")
for key,ref in auteurindex.items():
    auteura,indexa = key,ref
    if debug :
        print("\nauteura.title() : ",auteura.title())
        print("indexa : ",indexa)

#livre
if debug:
    print("trouve ref pour : ",lrplivre)
rkt = {"Mots": lrplivre,"livres":"livres"}
soup = req_mtd_post(rkt)
livreindex = ret_livr_indx(soup)
if len(livreindex) != 1: sys.exit("Désolé")
for key,ref in livreindex.items():
    livrel,indexl = key,ref
    if debug :
        print("\livrel.title() : ",livrel.title())
        print("indexl : ",indexl)

#livres attribués à un auteur connu
if debug:
    print("\nTrouve ref pour les livres de : ",lrpauteur," connu comme : ",auteura.title(),".")
rqt=indexa
soup = req_mtd_get(rqt)


#livre et auteur connu
if debug:
    print("\nTrouve ref pour les publication de : ",livrel.title()," de : ",auteura.title(),".")
rqt="/livres/EditionsLivre.asp?"+indexl.split("?")[1]+"&"+indexa.split("?")[1]
soup = req_mtd_get(rqt)


"""
import re
import requests

s = '<a class=gb1 href=[^>]+>'
r = requests.get('https://www.google.com/?q=python')
result = re.search(s, r.text)

print result.group(0)
If you simply need the list of all matches you can use: re.findall(s, r.text)

share  follow
"""

"""
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
