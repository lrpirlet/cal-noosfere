#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
#
# Note: If this work (done to learn both python and the Hyper Text Markup Language) finds its way to the public domain, so be it.
# I have no problem with, and reserve the right to ignore, any error, choice and poor optimization.
# I use it, it is MY problem... You use it, it is YOUR problem.
# For example, my mother language is French and my variable's names are MY choise for MY easy use...
# Anyway, I'll comment (or not) in english or in french or in both depending when I write it (no comment please :-) )
#
# noosfere is a database of books, volumes, covers, authors, translators, cover designers, critics, critic's author, movies adaptation...
# noosfere is NOT commercial, it is the DB of an association of authors, readers, editors... see about.txt
# last but not least noosfere is in french ONLY: noosfere defines itself as "nooSFere : encyclopédie francophone de Science-Fiction."
#
# A volume has in common with a book the author and the title but not the cover, not the editor, not the isbn, not.."
# I want the information about a volume... I want a coherent information.
#
# In order to collect the information about a volume one must use either the ISBN, the author and the title or at least the title
#
# If the ISBN exists a search in noosfere points to a serie of volumes (yet only one book :-) )
#
# if the author is the best known identifier a search in noosfere points to an author's list of books (or a list of authorss :-( )
# out of this list, a match to the title will point to a serie of volumes
#
# if the title is the only reference, a search in noosfere will output a list of books sorted by best mactch along with a score
# again a book will point to a serie of volume
#
# out of the volume list one must choose the best candidate to get a coherent set of volumes attributes (cover, isbn, editor, critics, serie, serie #, etc...
#
#
# the nice think about noosfere is the power of the search (each word may be "ANDed, exact or fuzzy match, etc...)
# the result gives a LOT of information about the book, author, translator...
# and the nice think about calibre is the possibility to insert working url in the comments and in the catalog
#

__license__   = 'GPL v3'
__copyright__ = '2021, Louis Richard Pirlet'
__docformat__ = 'restructuredtext en'           # whatever that means???

# those are python code that are directly available in calibre closed environment (test import... using calibre-debug)
import urllib                                   # to access the web
from bs4 import BeautifulSoup as BS             # to dismantle and manipulate HTTP (HyperText Markup Language)
#import sys                                      # so I can access sys (mainly during development, probably useless now)
import time                                     # guess that formats data and time in a common understanding
from queue import Empty, Queue                  # to submit jobs to another process (worker use it to pass results to calibre
from difflib import SequenceMatcher as SM
''' difflib has SequenceMatcher to compare 2 sentences
s1 = ' It was a dark and stormy night. I was all alone sitting on a red chair. I was not completely alone as I had three cats.'
s2 = ' It was a murky and stormy night. I was all alone sitting on a crimson chair. I was not completely alone as I had three felines.'
result = SM(None, s1, s2).ratio()
result is 0.9112903225806451... anything above .6 may be considered similar
'''

# the following make some calibre code available to my code
from calibre.ebooks.metadata.sources.base import (Source, Option)
from calibre.ebooks.metadata import check_isbn
from calibre.utils.icu import lower
from calibre.utils.localization import get_udc

def urlopen_with_retry(log, dbg_lvl, br, url, rkt, who):
    # this is an attempt to keep going when the connection to noosfere fails for no (understandable) reason
    #
    debug=dbg_lvl & 4
    if debug:
        log.info(who, "In urlopen_with_retry(log, dbg_lvl, br, url, rkt, who)")

    tries, delay, backoff=4, 3, 2
    while tries > 1:
        try:
            sr = br.open(url,data=rkt,timeout=30)
            log.info(who,"(ret_soup) sr.getcode()  : ", sr.getcode())
            if debug:
                log.info(who,"url_vrai      : ", sr.geturl())
                log.info(who,"sr.info()     : ", sr.info())
                log.info(who,"ha ouais, vraiment? charset=iso-8859-1... ca va mieux avec from_encoding...")
            return (sr, sr.geturl())
        except urllib.error.URLError as e:
            if "500" in str(e):
                log.info("\n\n\n"+who,"HTTP Error 500 is Internal Server Error, sorry\n\n\n")
                raise Exception('(ret_soup) Failed while acessing url : ',url)
            else:
                log.info(who,"(urlopen_with_retry)", str(e),", will retry in", delay, "seconds...")
                time.sleep(delay)
                delay *= backoff
                tries -= 1
                if tries == 1 :
                    log.info(who, "exception occured...")
                    log.info(who, "code : ",e.code,"reason : ",e.reason)
                    raise Exception('(ret_soup) Failed while acessing url : ',url)

def ret_soup(log, dbg_lvl, br, url, rkt=None, who=''):
    # Function to return the soup for beautifullsoup to work on.
    #
    debug=dbg_lvl & 4
    if debug:
        log.info(who, "In ret_soup(log, dbg_lvl, br, url, rkt=none, who='[__init__]')")
        log.info(who, "br  : ", br)
        log.info(who, "url : ", url)
        log.info(who, "rkt : ", rkt)
    # Note: le SEUL moment ou on doit passer d'un encodage des characteres a un autre est quand on reçoit des donneées
    # d'un site web... tout, absolument tout, est encodé en uft_8 dans le plugin... J'ai vraiment peiné a trouver l'encodage 
    # des charracteres qui venaient de noosfere... Meme le decodage automatique se plantait...
    # J'ai du isoler le creatioon de la soup et du decodage dans la fonction ret_soup().
    # variable "from_encoding" isolée pour trouver quel est l'encodage d'origine... 
    # il n'est pas improbable que ce soit ça que le site va modifier dans le futur...
    #
    # variable "from_encoding" isolated to find out what is the site character encoding... The announced charset is WRONG
    # Even auto decode did not always work... I knew that my setup was wrong but it took me a while...
    # Maybe I should have tried earlier the working solution as the emitting node is MS
    # (Thanks MS!!! and I mean it as I am running W10.. :-) but hell, proprietary standard is not standard)...
    # It decode correctly to utf_8 with windows-1252 forced as from_encoding
    # watch-out noosfere is talking about making the site better... ;-}
    #
    from_encoding="windows-1252"


    log.info(who, "Accessing url : ", url)
    if rkt :
        log.info(who, "search parameters : ",rkt)
        rkt=urllib.parse.urlencode(rkt).encode('ascii')
        if debug: log.info(who, "formated parameters : ", rkt)

    resp = urlopen_with_retry(log, dbg_lvl, br, url, rkt, who)
    if debug: log.info(who,"...et from_encoding, c'est : ", from_encoding)

    sr, url_ret = resp[0], resp[1]

    soup = BS(sr, "html5lib", from_encoding="windows-1252")
    if debug:
#        log.info(who,"soup.prettify() :\n",soup.prettify())               # très utile parfois, mais que c'est long...
        log.info(who,"(ret_soup) return (soup,sr.geturl()) from ret_soup\n")
    return (soup, url_ret)

def verify_isbn(log, dbg_lvl, isbn_str, who=''):
    # isbn_str est brute d'extraction... la fonction renvoie un isbn correct ou "invalide"
    # Notez qu'on doit supprimr les characteres de separation et les characteres restants apres extraction
    # et que l'on traite un mot de 10 ou 13 characteres.
    #
    # isbn_str is strait from extraction... function returns an ISBN maybe correct ...or not
    # Characters irrelevant to ISBN and separators inside ISBN must be removed,
    # the resulting word must be either 10 or 13 characters long.
    #
    debug=dbg_lvl & 4
    if debug:
        log.info("\nIn verify_isbn(log, dbg_lvl, isbn_str)")
        log.info("isbn_str         : ",isbn_str)

    for k in ['(',')','-',' ']:
        if k in isbn_str:
            isbn_str=isbn_str.replace(k,"")
    if debug:
        log.info("isbn_str cleaned : ",isbn_str)
        log.info("return check_isbn(isbn_str) from verify_isbn\n")
    return check_isbn(isbn_str)         # calibre does the check for me after cleaning...

def ret_clean_text(log, dbg_lvl, text, swap=False, who=''):
    # for noosfere search to work smoothly, authors and title needs to be cleaned
    # we need to remove non significant characters and remove useless space character
    #
    debug=dbg_lvl & 4
    if debug:
        log.info("\nIn ret_clean_txt(self, log, text, swap =",swap,")")
        log.info("text         : ", text)

    # Calibre per default presents the author as "Firstname Lastname", cleaned to be become "firstname lastname"
    # Noosfere present the author as "LASTNAME Firstname", let's get "Firstname LASTNAME" cleaned to "firstname lastname"
    #
    for k in [',','.','-',"'",'"','(',')']:             # yes I found a name with '(' and ')' in it...
        if k in text:
            text = text.replace(k," ")
    text=" ".join(text.split())

    if swap:
        if debug:
            log.info("swap name and surname")
        nom=prenom=""
        for i in range(len(text.split())):
            if (len(text.split()[i])==1) or (not text.split()[i].isupper()):
                prenom += " "+text.split()[i]
            else:
                nom += " "+text.split()[i]
        text=prenom+" "+nom
        if debug: log.info("text         : ", text)

    if debug:
        log.info("cleaned text : ", text)
        log.info("return text from ret_clean_txt")

    return lower(get_udc().decode(text))

class noosfere(Source):
    # see https://manual.calibre-ebook.com/fr/plugins.html#calibre.ebooks.metadata.sources.base.Source
    # and https://manual.calibre-ebook.com/fr/_modules/calibre/ebooks/metadata/sources/base.html#Source

    name                    = 'noosfere DB'
    description             = _('Source extention: downloads and sets metadata from noosfere.org for selected volumes')
    author                  = 'Louis Richard Pirlet'
    version                 = (0, 7, 0)
    minimum_calibre_version = (5, 11, 0)

    ID_NAME = 'noosfere'
    capabilities = frozenset(['identify', 'cover'])
    touched_fields = frozenset(['title', 'authors', 'identifier:isbn', 'identifier:nsfr_id', 'languages',
                                'comments', 'publisher', 'pubdate', 'series', 'tags'])
    has_html_comments = True
    supports_gzip_transfer_encoding = True

    # Since the noosfere is written in french for french talking poeple, I
    # took the liberty to write the following information in french. I will
    # comment with a translation in the english language.

                                    #config help message: noosfere is a database that presents information
                                    #about French books, tagged as science-fiction. Those informations span
                                    #from author to films made of the books, including translators,
                                    #illustrators, critics... and of course there work. The book that were
                                    #published several time are exposed as a "volume". Each of those volumes
                                    #share the authors and the book content, they MAY share, or not, the
                                    #cover, the editor, the editor's collection and the associated order
                                    #number, the resume, the critics,etc.... The choice of the volume is done
                                    #by the program. One may somewhat influence the choice through the dialog
                                    #box `priorité de tri´. On the other hand, there is no offical way to
                                    #programmaticaly update a custom column. So There is a tick box that will
                                    #push the information along with the publisher. Please read the doc to
                                    #understand how to put it back later in the right place with a right format.

    config_help_message = '<p>'+_(" noosfere est une base de donnée qui propose des informations"
                                  " à propos des ouvrages, de genre science fiction, disponibles en langue française."
                                  " Ces informations vont de l'auteur aux films produits sur base de l'ouvrage en"
                                  " passant par les auteurs, les traducteurs, les illustrateurs, les critiquess..."
                                  " et bien sur, leurs oeuvres. Les livres qui ont été publiés plusieurs fois"
                                  " sont repris chacun sous un volume dont est exposé l'ISBN, la date de dépot legal"
                                  " (repris sous la date de publication, souvent méconnue), la couverture, l'éditeur,"
                                  " la collection de l'editeur et son numèro d'ordre. Le choix, programmé, du volume"
                                  " est quelque peu paramétrable par la boite de dialogue `priorité de tri´. "
                                  " D'autre part, il n'existe pas de moyens officiels de remplir une colonne définie"
                                  " par l'utilisateur. Pour rester dans les clous, je propose de remplir le champs"
                                  " de l'editeur avec, conjointement à celui-ci, la collection et son numero d'ordre."
                                  " Une petite procédure, décrite dans la doc devrait remettre tout en ordre."
                                  )

    # priority handling, a choice box that propose to set the priority over
    # the oldest published volume with a preference for an ISBN balanced for a maximum of comments
    # the latest published volume with a preference for an ISBN balanced for a maximum of comments
    # the oldest balanced for a maximum of comments
    # the latest balanced for a maximum of comments
    # the very oldest
    # the very latest
    # note that the selected volume will have the most represented editor
    # (if editor x reedited 4 time the book, and editor Y only once,
    # editor x will certainly be selected)
    # see algorithm explanation in worker.py 'ret_top_vol_indx(self, url, book_title)'

    PRIORITY_HANDLING={
                       '0_oldest_with_isbn':_("le plus ancien pondéré, préfère un isbn"),
                       '1_latest_with_isbn':_("le plus récent pondéré, préfère un isbn"),
                       '2_oldest':_("un plus ancien pondéré"),
                       '3_latest':_("un plus recent pondéré"),
                       '4_very_oldest':_("vraiment plus ancien"),
                       '5_very_latest':_("vraiment plus recent")
                        }

    options = (
            Option(
                   'fat_publisher',
                   'bool',
                   False,
                   _("Ajoute collection et son numéro d'ordre au champ èditeur"),       # add the editor's collection and the associated order number to the publisher field
                   _("Cochez cette case pour ajouter la collection et son numéro d'ordre au champs de l'éditeur."
                     "Voir LIS-MOI editeur_collection_seriel-code.txt")                 # check this box to enable... see README publisher_collection_seriel-code.txt
                   ),
            Option(
                   'debug_level',
                   'number',
                   0,
                   _('Loquacité du journal, de 0 à 7'),                                                     # verbosity of the log
                   _('Le niveau de loquacité. O un minimum de rapport, 1 rapport etendu de __init__,'       # the level of verbosity. value 0 will output the minimum,
                     ' 2 rapport étendu de worker, 4 rapport etendu des annexes... La somme 3, 5 ou 7'      # 1 debug messages of __init__, 2 debug messages of worker
                     ' peut etre introduite. Ainsi 7 donne un maximun de rapport. Note: ce sont les 3'      # 4 debug level of accessory code... 3, 5 or 7 is the sum
                     ' derniers bits de debug_level en notation binaire')                                   # of the value defined above. In fact it is a bitwise flag
                   ),                                                                                       # spread over the last 3 bits of debug_level
            Option(
                   'priority_handling',
                   'choices',
                   '0_oldest_with_isbn',
                   _('priorité de tri:'),
                   _("Priorité de tri du volume."),    # how to push the priority over the choice of the volume
                   choices=PRIORITY_HANDLING
                   ),
            Option(
                   'requested_editor',
                   'string',
                   None,
                   _("impose un éditeur"),                                                                  # impose a publisher
                   _("le volume sera choisi chez l'éditeur le plus representé... SAUF:"                     # the volume is picked-up from the most prevalent publisher
                     " Remplir ce champ pour forcer un éditeur defini... DOIT"                              # EXCEPTED: fill this field to force the publisher wanted
                     " ETRE UN MATCH PARFAIT sinon le volume sera choisi sans tenir compte"                 # MUST BE A PERFECT MATCH else the volume will ne picked-up
                     " de l'éditeur.")                                                                      # without consideration to the publisher
                   ),
            )

    # this defines a method to access both the code and the data in the object
    @property
    def priority_handling(self):
        x = getattr(self, 'prio_handling', None)
        if x is not None:
            return x
        prio_handling = self.prefs['priority_handling']
        if prio_handling not in self.PRIORITY_HANDLING:
            prio_handling = sorted(self.PRIORITY_HANDLING.items())[0]    # sort the dict to make a list and select first item (that should be the default)
        return prio_handling

    @property
    def extended_publisher(self):
        x = getattr(self, 'ext_pub', None)
        if x is not None:
            return x
        ext_pub = self.prefs.get('fat_publisher', False)
        return ext_pub

    @property
    def dbg_lvl(self):
        x = getattr(self, 'dl', None)
        if x is not None:
            return x
        dl = self.prefs.get('debug_level', False)
        return dl

    @property
    def must_be_editor(self):
        x = getattr(self, 'te', None)
        if x is not None:
            return x
        te = self.prefs.get('requested_editor', None)
        return te

    # copied from other working metadata source (thanks to David Forrester and the Kobo Books Metadata source)
    def get_cached_cover_url(self, identifiers):
        # I guess this routine returns an url that was discovered somewhere else and put into cache
        # probably using cache_identifier_to_cover_url in the worket.py
        # as ISBN is missing sometime in noosfere
        # as noosfere does not provide any proprietary id
        # I will use nsfr_id, a combination of bk_<significant part of book_url>_vl_<significant part of vol_url>
        # this should allow to go directly to the book page (that could be the vol page if there is only one vol for the book)
        #
        url = None
        nsfr_id = identifiers.get('nsfr_id', None)
        if nsfr_id is None:
            isbn = identifiers.get('isbn', None)
            if isbn is not None:
                nsfr_id = self.cached_isbn_to_identifier(isbn)
        if nsfr_id is not None:
            url = self.cached_identifier_to_cover_url(nsfr_id)
        return url

    def ret_author_index(self, log, br, authors):
        # Trouve la reference de l'auteur dans la soupe de noosfere
        # retourne author_index, un dictionnaire avec key=AUTEUR, val=href
        # L'idée est de renvoyer UNE seule reference... trouver l'auteur est primordial si isbn is indisponible
        #
        # Find author references in the soup produced by noosfere, return author_index a dictionary with key=author, val=href
        # the idea is to find ONE single reference... to get the author is important if isbn is unavailable
        #
        debug=self.dbg_lvl & 1
        log.info("\nIn ret_author_index(soup)")
        if debug:
            log.info("authors    : ", authors)
        all_author_index={}
        author_index=[]

        # try to get a short list of authors using "MOTS-CLEFS" match

        for j in range(len(authors)):
            rkt = {"Mots":authors[j],"auteurs":"auteurs","ModeMoteur":"MOTS-CLEFS","ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}
            url = "https://www.noosfere.org/livres/noosearch.asp"
            soup = ret_soup(log, self.dbg_lvl, br, url, rkt=rkt )[0]
            tmp_ai=soup.select('a[href*="auteur.asp"]')
            if len(tmp_ai):
                for i in range(len(tmp_ai)):
                    url_author, author, perta=tmp_ai[i]["href"], tmp_ai[i].text, tmp_ai[i].find_previous('tr').select_one('td').text
                    ratio = SM(None, ret_clean_text(log, self.dbg_lvl, author,swap=True), authors[j]).ratio()
                    if debug:
                        log.info("pertinence : ", perta, end=" ; ")
                        log.info("SM.ratio : {:.3f}".format(ratio), end=" ; ")
                        log.info("url_author : ", url_author, end=" ; ")
                        log.info("authors[j] : ", authors[j], end=" ; ")
                        log.info("author : ", ret_clean_text(log, self.dbg_lvl, author))
                    if ratio > .6 :
                        all_author_index[url_author]=[ratio, author]

            if not len(all_author_index):                          # failed the short list, let's go for the long list using "LITTERAL" match
                if debug: log.info("exact match failed, trying fuzzy match")
              # return self.ret_author_index(self, log, br, authors, ModeMoteur="LITTERAL")
              # ca marche pas... ret_author_index() got multiple values for argument 'ModeMoteur'
              # this is NOT a function but a class method
              # it is possible to move the common part of this code below, but my mind refuses to understand the change
              # when debugging... so duplicate the code (maybe an optimiseur later will make it... m'en fout)
                for j in range(len(authors)):
                    rkt = {"Mots":authors[j],"auteurs":"auteurs","ModeMoteur":"LITTERAL","ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}
                    url = "https://www.noosfere.org/livres/noosearch.asp"
                    soup = ret_soup(log, self.dbg_lvl, br, url, rkt=rkt )[0]
                    tmp_ai=soup.select('a[href*="auteur.asp"]')
                    if len(tmp_ai):
                        for i in range(len(tmp_ai)):
                            url_author, author, perta=tmp_ai[i]["href"], tmp_ai[i].text, tmp_ai[i].find_previous('tr').select_one('td').text
                            ratio = SM(None, ret_clean_text(log, self.dbg_lvl, author,swap=True), authors[j]).ratio()
                            if debug:
                                log.info("pertinence : ", perta, end=" ; ")
                                log.info("SM.ratio : {:.3f}".format(ratio), end=" ; ")
                                log.info("url_author : ", url_author, end=" ; ")
                                log.info("authors[j] : ", authors[j], end=" ; ")
                                log.info("author : ", ret_clean_text(log, self.dbg_lvl, author))
                            if ratio > .6 :
                                all_author_index[url_author]=[ratio, author]

        sorted_author_index=dict(sorted(all_author_index.items(), key=lambda x: x[1][0],reverse=True))

        if debug: log.info("sorted_author_index :\n",sorted_author_index)

        # With python 3.6 onward, the standard dict type maintains insertion order by default.
        # Python 3.7 elevates this implementation detail to a language specification,
        # noosfere sort the hightest pertinence first (the most probable author comes out first)
        # so, I have no need to sort on pertinence field (would be different for calibre below Version 5)
        #
        # we only consider those with the highest pertinence, we limit to when the pertinence drops to less than half of the maximum
        #

        count=0
        for key,ref in sorted_author_index.items():
            count+=1
            url_author, ratio, name_author = key, ref[0], ref[1]
            author_index.append(url_author)
            if debug:
                log.info("ratio : ", ratio, end=" ; ")
                log.info("author     : ", name_author, end=" ; ")
                log.info("url_author : ", url_author, end=" ; ")
                log.info("count : ",count)
#                log.info("author_index : ",author_index)       # may be long
            if count == 8 : break

        if debug: log.info('return from ret_author_index')
        return author_index

    def ret_book_per_author_index(self, log, br, author_index, title, book_index):
        # Find the books references of a known author from the returned soup for noosfere
        # returns a dict "book_per_author_index{}" with key as title and val as the link to the book
        # Idea is to send back a few references that hopefully contains the title expected
        #
        # Trouver la reference des livres d'un auteur connu dans la soupe produite par noosfere
        # retourne "book_per_author_index{}", un dictionnaire avec key=titre, val=href
        # L'idée est de renvoyer serie de reference, dont on extrait les livres proches du titre de calibre
        #
        # now that we have a list of authors, let's get all the books associated with them
        # The "book_per_author_index" dictionnary will contain all book's references...
        # If a book has a common url it will be overwritten by the following author, ensuring a list of unique books
        #
        debug=self.dbg_lvl & 1
        log.info("\nIn ret_book_per_author_index(self, log, br, author_index, title, book_index)")
        if debug:
            log.info("author_index : ",author_index)
            log.info("title        : ",title)
            log.info("book_index   : ",book_index)

        book_per_author_index={}
        unsorted_book_index={}

        for i in range(len(author_index)):
            rqt= author_index[i]+"&Niveau=livres"
            url="https://www.noosfere.org"+rqt
            soup = ret_soup(log, self.dbg_lvl, br, url)[0]
            tmp_bpai=soup.select('a[href*="ditionsLivre.asp"]')
            for i in range(len(tmp_bpai)):
                book_title=tmp_bpai[i].text.lower()
                book_url=(tmp_bpai[i]["href"].replace('./','/livres/').split('&'))[0]
                ratio = SM(None, title, ret_clean_text(log, self.dbg_lvl, book_title)).ratio()
                if debug:
                    log.info("SM.ratio : {:.3f}".format(ratio),end=" ; ")
                    log.info("book_url : ",book_url,end=" ; ")
                    log.info('tmp_bpai[i]["href"] : ',tmp_bpai[i]["href"],end=" ; ")
                    log.info("book_title : ",book_title)
                if ratio > .6 :
                    unsorted_book_index[ratio]=[book_url, "", book_title]
                if ratio == 1:
                    unsorted_book_index={}
                    unsorted_book_index[ratio]=[book_url, "", book_title]
                    break                        # we have a perfect match no need to go further in the author books
                                                 # and I know it could cause problem iff several authors produce an identical title

            sorted_book_index=dict(sorted(unsorted_book_index.items(),reverse=True))
            for key,ref in sorted_book_index.items():
                book_url = ref[0]
                book_index[book_url] = book_title
                log.info('book_index[book_url] = book_title : ',book_index)

            if ratio == 1:
                log.info("Perfect match, we got it and we can stop looking further")
                break                           # we have a perfect match no need to examine other authors

        if debug: log.info('return book_index from ret_book_per_author_index\n')
        return book_index

    def ISBN_ret_book_index(self, log, br, isbn, book_index):
        # Trouver la reference d'un livre (titre ou ISBN) dans la soupe produite par noosfere
        # retourne book_index{}, un dictionnaire avec key=book_url, val=title
        # L'idée est de trouver UNE seule reference...
        # Attention: on retourne une reference qui peut contenir PLUSIEURs volumes
        # C'est a dire: différents editeurs, différentes re-éditions et/ou, meme, un titre different... YESss)
        #
        # Find the book's reference (either title or ISBN) in the returned soup from noosfere
        # returns book_index{}, a dictionnary with key=book_url, val=title
        # The idea is to find ONE unique reference...
        # Caution: the reference may contains several volumes,
        # each with potentialy a different editor, a different edition date,... and even a different title
        #
        debug=self.dbg_lvl & 1
        log.info("\nIn ISBN_ret_book_index(self, log, br, isbn, book_index)")

        # if isbn valid then we want to select exact match (correspondance exacte = MOTS-CLEFS)
        rkt={"Mots": isbn,"livres":"livres","ModeMoteur":"MOTS-CLEFS","ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}
        url = "https://www.noosfere.org/livres/noosearch.asp"
        soup = ret_soup(log, self.dbg_lvl, br, url, rkt=rkt )[0]
        tmp_rbi=soup.select('a[href*="ditionsLivre.asp"]')
        if len(tmp_rbi):
            for i in range(len(tmp_rbi)):
                if debug:
                    log.info("tmp_rbi["+str(i)+"].text, tmp_rbi["+str(i)+"]['href'] : ",tmp_rbi[i].text,tmp_rbi[i]["href"])
                book_index[tmp_rbi[i]["href"]]=tmp_rbi[i].text

        if debug:
            log.info("book_index : ",book_index)
            log.info("return book_index from ISBN_ret_book_index\n")
        return book_index

    def identify(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
        # this is the entry point...
        # Note this method will retry without identifiers automatically... read can be resubmitted from inside it
        # if no match is found with identifiers.
        #

        log.info('self.dgb_lvl            : ', self.dbg_lvl)
        log.info('self.extended_publisher : ', self.extended_publisher)
        log.info('self.priority_handling  : ', self.priority_handling)
        log.info('self.must_be_editor     : ', self.must_be_editor)

        debug=self.dbg_lvl & 1
        log.info('\nEntering identify(self, log, result_queue, abort, title=None, authors=None,identifiers={}, timeout=30)')
        if debug:
            log.info('log          : ', log)
            log.info('result_queue : ', result_queue)
            log.info('abort        : ', abort)
            log.info('title        : ', title)
            log.info('authors      : ', authors, type(authors))
            log.info('identifiers  : ', identifiers, type(identifiers))
            log.info('\n')

        br = self.browser

        isbn = identifiers.get('isbn', None)
        if isbn: isbn = verify_isbn(log, self.dbg_lvl, isbn)
        log.info('ISBN value is : ', isbn)

        # the nsfr_id is designed to be the significant part of the url:
        # that is the number after the "=" in the url containing "niourf.asp?numlivre"
        # on can force the access to a particular volume by setting the value of nsfr_id to vl$<number>
        # could be an entry point if I can make sure that noosfere DB is alone and in interactive mode...
        nsfr_id = identifiers.get('nsfr_id', None)
        log.info('nsfr_id value is : ', nsfr_id)

        log.info('"Clean" both the authors list and the title... ')
        for i in range(len(authors)):
            authors[i] = ret_clean_text(log, self.dbg_lvl, authors[i])
        title = ret_clean_text(log, self.dbg_lvl, title)

        log.info('getting one or more book url')
        book_index={}        # book_index={} is a dict: {key:ref} with: book_url, book_title = key, ref
        if nsfr_id:
            log.info('trying noosfere id, ', nsfr_id )
            nsfr = nsfr_id.split("$")
            if "bk" in nsfr[0] :
                url = "/livres/EditionsLivre.asp?numitem="+nsfr[1]
                if "vl" in nsfr[2] :
                    url = "/livres/niourf.asp?numlivre="+nsfr[3]
                book_index[url]=title
            elif "vl" in nsfr[0] :
                url = "/livres/niourf.asp?numlivre="+nsfr[1]
                book_index[url]=title
            else:
                log.info('noosfere id not valid...')

        if not book_index:
            log.info('trying ISBN', isbn)
            if isbn:
                book_index = self.ISBN_ret_book_index(log, br, isbn, book_index)
                if not len(book_index):
                    log.error("This ISBN was not found: ", isbn, "trying with title", title,"and author", authors)
                    return self.identify(log, result_queue, abort, title=title, authors=authors, timeout=timeout)
            elif title and authors:
                log.info('trying using authors and title')
                author_index=self.ret_author_index(log, br, authors)
                if len(author_index):
                    book_index = self.ret_book_per_author_index(log, br, author_index, title, book_index)
                if not len(author_index):
                    log.info("Désolé, aucun auteur trouvé avec : ",authors)
                    return
        # here maybe try with title alone... a dessiner lrp todo... ouais peut-etre pour le cas ou l'auteur serait trop noyé dans une masse de noms similaires

        if not book_index:
            log.error("No book found in noosfere... ")
            return

        if abort.is_set():
            log.info('abort was set... aborting... ')
            return

        tmp_list=[]
        for key,ref in book_index.items():
            book_url, book_title = key, ref
            if debug:log.info("\nbook_url, book_title : ", book_url,", ", book_title)
            tmp_list.append((book_url, book_title))

        from calibre_plugins.noosfere.worker import Worker
        workers = [Worker(log, data[0], data[1], isbn, result_queue, br, i, self, self.dbg_lvl) for i, data in enumerate(tmp_list)]

        for w in workers:
            w.start()
            # Don't send all requests at the same time
            time.sleep(0.2)

        while not abort.is_set():
            a_worker_is_alive = False
            for w in workers:
                w.join(0.2)
                if abort.is_set():
                    log.info('abort was set while in loop... aborting... ')
                    break
                if w.is_alive():
                    a_worker_is_alive = True
            if not a_worker_is_alive:
                break

        if debug: log.info("return None from identify")
        return None


    def download_cover(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
        # willl download cover from Noosfere provided it was found (and then cached)... If not, it will
        # run the metadata download and try to cache the cover url...

        cached_url = self.get_cached_cover_url(identifiers)
        if cached_url is None:
            log.info('No cached cover found, running identify')
            rq = Queue()
            self.identify(log, rq, abort, title=title, authors=authors, identifiers=identifiers)
            if abort.is_set():
                return
            results = []
            while True:
                try:
                    results.append(rq.get_nowait())
                except Empty:
                    break
            results.sort(key=self.identify_results_keygen(title=title, authors=authors, identifiers=identifiers))
            for mi in results:
                cached_url = self.get_cached_cover_url(mi.identifiers)
                if cached_url is not None:
                    break
        if cached_url is None:
            log.info('No cover found')
            return

        if abort.is_set():
            return

        br = self.browser
        log('Downloading cover from:', cached_url)
        try:
            cdata = br.open_novisit(cached_url, timeout=timeout).read()
            result_queue.put((self, cdata))
        except:
            log.exception('Failed to download cover from:', cached_url)

####################### test section #######################

if __name__ == '__main__':

    # Run these tests from the directory contatining all files needed for the plugin (the files that go into the zip file)
    # that is: __init__.py, plugin-import-name-noosfere.txt and optional .py such as worker.py, ui.py
    # issue in sequence:
    # calibre-customize -b .
    # calibre-debug -e __init__.py
    # attention: on peut voir un message prévenant d'une erreur... en fait ce message est activé par la longueur du log...
    # Careful, a message may pop up about an error... however this message pops up function of the lengh of the log...
    # anyway, verify... I have been caught at least once

    from calibre.ebooks.metadata.sources.test import (test_identify_plugin, title_test, authors_test, series_test)
    test_identify_plugin(noosfere.name,
        [

##            ( # A book with ISBN specified not in noosfere
##                {'identifiers':{'isbn': '9782265070769'}, 'title':'Le chenal noir', 'authors':['G.-J. Arnaud']},
##                [title_test("	Le Chenal noir", exact=True), authors_test(['G.-J. Arnaud']), series_test('La Compagnie des glaces - Nouvelle époque',2)]
##            ),

##            ( # A book with no ISBN specified
##                {'identifiers':{}, 'title':"L'Heure de 80 minutes", 'authors':['b ALDISS']},
##                [title_test("L'Heure de 80 minutes", exact=True), authors_test(['Brian ALDISS']), series_test('',0)]
##            ),

##            ( # A book with an ISBN
##                {'identifiers':{'isbn': '978-2-84344-061-0'}, 'title':"Le Printemps d'Helliconia", 'authors':['B.W. Aldiss']},
##                [title_test("Le Printemps d'Helliconia", exact=True), authors_test(['Brian Aldiss']), series_test('Helliconia', 1.0)]
##            ),

##            ( # A book with an ISBN
##                {'identifiers':{'isbn': '2277214094'}, 'title':"La Patrouille du temps", 'authors':['Poul Anderson']},
##                [title_test("La Patrouille du temps", exact=True), authors_test(['Poul Anderson']), series_test('La Patrouille du Temps', 1.0)]
##            ),

            ( # A book with no ISBN
                {'identifiers':{}, 'title':"La Septième saison", 'authors':['Pierre Suragne']},
                [title_test("La Septième saison", exact=True), authors_test(['Pierre Suragne']), series_test('', 0)]
            ),

##            ( # A book with a HTTP Error 500
##                {'identifiers':{'isbn': '2-290-04457-1'}, 'title':"Le Monde de l'exil", 'authors':['David BRIN']},
##                [title_test("Le Monde de l'exil", exact=True), authors_test(['David Brin']), series_test('', 0)]
##            ),

        ])
