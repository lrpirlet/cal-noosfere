import re
from bs4 import BeautifulSoup as BS
import urllib
import urllib.request
import urllib.error
import sys

debug=1

lrpauteur = input("auteur : ")
#lrpauteur = "Eschbach Andreas"
if debug:
    if not len(lrpauteur):
#        lrpauteur="eschbach andreas"
#        lrpauteur="eschbach"
        lrpauteur="van vogt"

lrplivre = input("titre du livre : ")
if debug:
    if not len(lrplivre):
        #lrplivre = "kwest"          # un livre
        #lrplivre = "fondation"      # un tas de livres
        lrplivre = "cataplute "      # pas de livres

# noosfere accepts * to complete the name or the surname, trips on the dot in van vogt A.E.
lrpauteur=str(lrpauteur.replace(","," "))
lrpauteur=str(lrpauteur.replace(".","* "))
base_url="https://www.noosfere.org"
search_urn=base_url+"/noosearch_simple.asp"

def postrequest(requete):
    # Essayons un acces en mode post sur noosearch_simple.asp
    debug=0
    if debug: print("\nfuncion postrequest()")

    req=urllib.parse.urlencode(requete).encode('ascii')
    try: sr=urllib.request.urlopen(search_urn,req)
    except urllib.error.URLError as e:
        print("reason : ",e.reason)
        print("code : ",e.code)

    if debug:
        print("\ntype(sr) : ",type(sr))
        print("requete: ",requete)
        for i in sr.headers:
                print(i, " : ",sr.headers[i])

    soup = BS(sr, "html.parser")
    return soup

def ret_autr_indx(soup):
    # Trouve la reference de l'auteur dans la soupe produite par noosfere
    # retourne auteurindex, un dictionnaire avec key=AUTEUR, val=href
    debug=0
    auteurindex={}

    for child in soup.recursiveChildGenerator():
        if child.name=="span" and "class" in child.attrs:
            if 'resultat_search' in child["class"]:
                if debug:
                    print("\nfound 'resultat_search'")
                    print("child: ",child)
                    print("name : ", child.name)
                    print("text : ", child.text, "       type: ",type(child.text))
                    print("attributes", child.attrs, "      type:",type(child.attrs), "    len(child.attrs): ",len(child.attrs))
                    print("class: ",child["class"])
                    print('child.find_next("a"): ',child.find_next("a"))
                    print('child.find_next("a")["href"]: ',child.find_next("a")["href"])

                if "auteur.asp" in child.find_next("a")["href"]:
                    auteurindex[child.text]=(child.find_next("a")["href"])

    if debug: print("auteurindex: ",auteurindex)
    if debug: print("\nauteurindex : len(auteurindex) :",auteurindex," : ",len(auteurindex))

    if len(auteurindex) > 1:
        print("Sorry, too many author found, please input one of the following :")
        for key in auteurindex:
            print(key.title())
    elif len(auteurindex) < 1:
        print("Sorry could not find the author")
    return auteurindex

def ret_livr_indx(soup):
    # Trouver la reference d'un livre dans la soupe produite par noosfere
    # retourne livreindex, un dictionnaire avec key=titre, val=href
    debug=1
    if debug: print("\nfuntion ret_livr_indx()")

    req=urllib.parse.urlencode(requete).encode('ascii')
    try: sr=urllib.request.urlopen(search_urn,req)
    except urllib.error.URLError as e:
        print("reason : ",e.reason)
        print("code : ",e.code)

    if debug:
        print("\ntype(sr) : ",type(sr))
        print("requete: ",requete)
        for i in sr.headers:
                print(i, " : ",sr.headers[i])
    soup = BS(sr, "html.parser")
    livreindex={}
    for child in soup.recursiveChildGenerator():
        if child.name=="span" and "class" in child.attrs:
            if 'resultat_search' in child["class"]:
                if debug:
                    print("\nfound 'resultat_search'")
                    print("child: ",child)
                    print("name : ", child.name)
                    print("text : ", child.text, "       type: ",type(child.text))
                    print("attributes", child.attrs, "      type:",type(child.attrs), "    len(child.attrs): ",len(child.attrs))
                    print("class: ",child["class"])
                    print('child.find_next("a"): ',child.find_next("a"))
                    print('child.find_next("a")["href"]: ',child.find_next("a")["href"])
                if "EditionsLivre.asp" in child.find_next("a")["href"]:
                    livreindex[child.text]=(child.find_next("a")["href"])
    if debug: print("livreindex: ",livreindex)
    if len(livreindex) > 1:
        print("Sorry, too many author found, please input one of the following :\n")
        for key in livreindex:
            print(key.title())
    elif len(livreindex) < 1:
        print("Sorry could not find the author")
    return livreindex

def ret_isbn_indx():
    # essayons un acces en mode post sur noosearch_simple.asp pour trouver la reference d'un isbn
    # retourne livreindex, un dictionnaire avec key=titre, val=href
    debug=1
    if debug: print("ret_isbn_indx()")

#auteur
requete = {"Mots": lrpauteur}
soup = postrequest(requete)
auteurindex = ret_autr_indx(soup) # quel est l'indexe de l'auteur? auteur is a dictionary
if len(auteurindex) != 1: sys.exit("Désolé")
for key,ref in auteurindex.items():
    auteura,indexa = key,ref
    if debug :
        print("\nauteura.title() : ",auteura.title())
        print("indexa : ",indexa)

#livre
requete = {"Mots": lrplivre}
soup = postrequest(requete)
livreindex = ret_livr_indx(soup)




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
