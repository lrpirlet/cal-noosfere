#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
##from __future__ import (unicode_literals, division, absolute_import,
##                        print_function)
##
__license__   = 'GPL v3'
__copyright__ = '2021, Louis Richard Pirlet'
__docformat__ = 'restructuredtext en'

import urllib.request
import urllib.error
from bs4 import BeautifulSoup as BS
import sys
import time
from queue import Empty, Queue

from calibre.ebooks.metadata.sources.base import (Source, Option)
from calibre.ebooks.metadata import check_isbn
from calibre.utils.icu import lower

##import re
##try:
##    from urllib.parse import quote, unquote
##except ImportError:
##    from urllib import quote, unquote
##try:
##
##except ImportError:
##    from Queue import Empty, Queue
##import six
##from six import text_type as unicode
##
##from lxml.html import fromstring, tostring
##
##from calibre import as_unicode
##from calibre.utils.cleantext import clean_ascii_chars
##from calibre.utils.localization import get_udc

class noosfere(Source):

    name                    = 'noosfere DB'
    description             = _('Downloads and sets metadata and cover from noosfere.org over volumes (will force, potentially, low res cover image)')
    author                  = 'Louis Richard Pirlet'
    version                 = (0, 1, 0)
    minimum_calibre_version = (5, 11, 0)

    ID_NAME = 'noosfere'
    capabilities = frozenset(['identify', 'cover'])
    touched_fields = frozenset(['title', 'authors', 'identifier:isbn', 'rating', 'languages',
                                'comments', 'publisher', 'pubdate', 'series', 'tags'])
    has_html_comments = True

#    def get_book_url(self, identifiers):
#    def id_from_url(self, url):
#
# No need for the above, there is absolutely no  way to construct a direct link to a volume
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
#
# the result gives a LOT of information about the book, author, translator...
# and the nice think about calibre is the possibility to insert working url in the comments and in the catalog
#


    def get_cached_cover_url(self, identifiers):
        # I guess this routine returns an url that was discovered somewhere else and put into cache (how? where?)
        # probably using cache_identifier_to_cover_url in the worket.py
        # needs implementing... ISBN is the sole identifier
        #
        url = None
        lrpid = identifiers.get(self.ID_NAME, None)
        if lrpid is None:
            isbn = identifiers.get('isbn', None)
            if isbn is not None:
                lrpid = self.cached_isbn_to_identifier(isbn)
        if lrpid is not None:
            url = self.cached_identifier_to_cover_url(lrpid)
        return url

    def verify_isbn(self, log, isbn_str):
        # isbn_str est brute d'extraction... la fonction renvoie un isbn correct ou "invalide"
        # Notez qu'on doit supprimr les characteres de separation et les characteres restants apres extraction
        # et que l'on traite un mot de 10 ou 13 characteres.
        #
        # isbn_str is strait from extraction... function returns an ISBN maybe correct ...or not
        # Characters irrelevant to ISBN and separators inside ISBN must be removed,
        # the resulting word must be either 10 or 13 characters long.
        #
        debug=1
        if debug:
            log.info("\nIn verify_isbn(isbn_str)")
            log.info("isbn_str         : ",isbn_str)

        for k in ['(',')','-',' ']:
            if k in isbn_str:
                isbn_str=isbn_str.replace(k,"")
        if debug:
            log.info("isbn_str cleaned : ",isbn_str)
            log.info("return from verify_isbn\n")

        return check_isbn(isbn_str)         # calibre does the check for me after cleaning...

    def make_soup(self, log, sr):
        # isolé pour trouver quel est l'encodage d'origine... ça marchait à peu pres sans forcer encodage d'entrée mais pas tout a fait
        # il n'est pas improbable que ce soit ça que le site va modifier dans le futur...
        #
        # function isolated to find out what is the site character encoding... The announced standard (in meta) is WRONG
        # requests was able to decode correctly, I knew that my setup was wrong but it took me a while...
        # Maybe I should have tried earlier the working solution as the emitting node is MS
        # (Thanks MS!!! and I mean it as I am running W10.. :-) but hell, proprietary standard is not standard)...
        # It decode correctly to utf_8 with windows-1252 forced as input encoding
        # watch-out noosfere is talking about making the site better... ;-}
        #
        debug=0        # set only to output soup (long, very long)

        if debug: log.info("\nIn make_soup(sr)")

        soup = BS(sr, "html.parser",from_encoding="windows-1252")
        if debug:
            log.info(soup.prettify())
            log.info('return from make_soup\n')

        if debug: log.info("return from make_soup\n")
        return soup

    def req_mtd_post(self, log, rkt, ModeMoteur = "LITTERAL"):
        # Accède en mode post sur <base_url>/livres/noosearch.asp
        # Access using "post" method over <base_url>/livres/noosearch.asp
        #
        debug=1
        if debug: log.info("\nIn req_mtd_post(log, rkt, ModeMoteur =",ModeMoteur,")")

        search_urn="https://www.noosfere.org/livres/noosearch.asp"
        base_rkt={"ModeMoteur":ModeMoteur,"ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}

        rkt.update(base_rkt)
        if debug: log.info("rkt",rkt)
        req=urllib.parse.urlencode(rkt).encode('ascii')
        try: sr=urllib.request.urlopen(search_urn,req,timeout=30)
        except TimeoutError:
            log.error("A network timeout occurred, do you have wide world web access?")
            sys.exit("désolé")
        except urllib.error.HTTPError as e:
            log.error("Une erreur envoyée par le site a été reçue.")
            log.error("code : ",e.code,"reason : ",e.reason)
            sys.exit("réponse d'erreur de l'url, désolé")
        except urllib.error.URLError as e:
            log.error("Une erreur envoyée par le site a été reçue.")
            log.error("reason : ",e.reason)
            sys.exit("réponse d'erreur de l'url, désolé")
        if debug:
            log.info("type(sr) : ",type(sr))
            log.info("sr.header : ")
            for i in sr.headers:
                    log.info(i, " : ",sr.headers[i])

        soup = self.make_soup(log, sr)
        if debug: log.info('return from req_mtd_post\n')
        return soup

    def ISBN_ret_book_index(self, log, isbn):
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
        if debug: log.info("\nIn ISBN_ret_book_index(soup)")

        rkt = {"Mots": isbn,"livres":"livres"}
        soup = self.req_mtd_post(log, rkt, ModeMoteur="MOTS-CLEFS")         # if isbn valid then we want to select exact match (correspondance exacte = MOTS-CLEFS)

        book_index={}

        tmp_rbi=soup.select('a[href*="editionsLivre.asp"]')

        if len(tmp_rbi):
            for i in range(len(tmp_rbi)):
                if debug:
                    log.info("tmp_rbi["+str(i)+"].text, tmp_rbi["+str(i)+"]['href'] : ",tmp_rbi[i].text,tmp_rbi[i]["href"])
#                book_index[tmp_rbi[i].text]=(tmp_rbi[i]["href"])
                book_index[time.time_ns()]=(tmp_rbi[i]["href"])             # time since epoch will be lrpid identifier to cache cover, should be different each time :-)

        if debug: log.info("return from ISBN_ret_book_index\n")
        return book_index

    def identify(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
        # this is the entry point...
        # Note this method will retry without identifiers automatically if no
        # match is found with identifiers.
        #
        debug=1
        if debug:
            log.info('\nEntering identify(self, log, result_queue, abort, title=None, authors=None,identifiers={}, timeout=30)')
            log.info('log          : ', log)
            log.info('result_queue : ', result_queue)
            log.info('abort        : ', abort)
            log.info('title        : ', title)
            log.info('authors      : ', authors, type(authors))
            log.info('identifiers  : ', identifiers)
            log.info('\n')

        isbn = identifiers.get('isbn', None)
        if isbn: isbn = self.verify_isbn(log, isbn)

        # for noosfere search to work smoothly, authors and title needs to be cleaned
        # we need to remove non significant characters
        # and remove useless space character

        for i in range(len(authors)):
            for k in [',','.','-']:
                if k in authors[i]:
                    authors[i] = authors[i].replace(k," ")
            authors[i] = lower(" ".join(authors[i].split()))
        if debug: log.info('authors cleaned : ',authors)

        for k in [',','.','-',"'",'"']:
            if k in title:
                title = title.replace(k," ")
        title = lower(" ".join(title.split()))
        if debug: log.info('title cleaned   : ',title)

        if isbn:
            book_index = self.ISBN_ret_book_index(log, isbn)
            if not len(book_index):
                log.error("This ISBN was not found: ", isbn, "trying with title and author")
                return self.identify(log, result_queue, abort, title=title, authors=authors, timeout=timeout)
        elif title and authors:
            # cherche les auteurs et les livres... trouve 0, 1 ou plus book_index
            log.info(' here a procedure to match books and authors that returns book_index {} with a form book_index[time.time_ns()]=url')
            book_index={}

        if not len(book_index):
            log.error("No book found in noosfere... ")
            return 

        for key,ref in book_index.items():
            lrpid,book_url = key,ref
            log.info("lrpid     : ",lrpid)
            log.info("book_url   : ",book_url)

        if abort.is_set():
            return

        sys.exit("ici on stoppe")

        from calibre_plugins.noosfere.worker import Worker
        workers = [Worker(data[0], data[1],  author_tokens, result_queue, br,      log, i,    self.category_handling, self) for i, data in enumerate(matches)]
        #def __init__(self, url  ,publisher, match_authors, result_queue, browser, log, relevance, category_handling, plugin, timeout=20):

        for w in workers:
            w.start()
            # Don't send all requests at the same time
            time.sleep(0.2)

        while not abort.is_set():
            a_worker_is_alive = False
            for w in workers:
                w.join(0.2)
                if abort.is_set():
                    break
                if w.is_alive():
                    a_worker_is_alive = True
            if not a_worker_is_alive:
                break

        return None



######################################### not tested, but needed ################################
#
    def download_cover(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
        log.info('\nEntering download_cover(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30)')
        log.info('log          : ', log)
        log.info('result_queue : ', result_queue)
        log.info('abort        : ', abort)
        log.info('title        : ', title)
        log.info('authors      : ', authors)
        log.info('identifiers  : ', identifiers)
        log.info('timeout      : ', timeout)

        cached_url = self.get_cached_cover_url(identifiers)
##        if cached_url is None:
##            log.info('No cached cover found, running identify')
##            rq = Queue()
##            self.identify(log, rq, abort, title=title, authors=authors,
##                    identifiers=identifiers)
##            if abort.is_set():
##                return
##            results = []
##            while True:
##                try:
##                    results.append(rq.get_nowait())
##                except Empty:
##                    break
##            results.sort(key=self.identify_results_keygen(
##                title=title, authors=authors, identifiers=identifiers))
##            for mi in results:
##                cached_url = self.get_cached_cover_url(mi.identifiers)
##                if cached_url is not None:
##                    break
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

    # Run these tests from the directory contatining all files needed for the plugin
    # that is, __init__.py, plugin-import-name-noosfere.txt and optional worker.py, ui.py
    # issue in sequence:
    # calibre-customize -b .
    # calibre-debug -e __init__.py

    from calibre.ebooks.metadata.sources.test import (test_identify_plugin, title_test, authors_test, series_test)
    test_identify_plugin(noosfere.name,
        [

##            ( # A book with no ISBN specified
##                {'title':"Turn Coat", 'authors':['Jim Butcher']},
##                [title_test("Turn Coat",
##                    exact=True), authors_test(['Jim Butcher']),
##                    series_test('Dresden Files', 11.0)]
##
##            ),
##
##            ( # A book with an ISBN
##                {'identifiers':{'isbn': '9780748111824'},
##                    'title':"Turn Coat", 'authors':['Jim Butcher']},
##                [title_test("Turn Coat",
##                    exact=True), authors_test(['Jim Butcher']),
##                    series_test('Dresden Files', 11.0)]
##
##            ),

            ( # A book with an ISBN
                {'identifiers':{'isbn': '2-221-10703-9'},
                    'title':"Le Printemps d'Helliconia", 'authors':['B.W. Aldiss']},
                [title_test("Le Printemps d'Helliconia",
                    exact=True), authors_test(['Brian Aldiss']),
                    series_test('Helliconia', 1.0)]

            ),

##            ( # A book with a KoboBooks id
##                {'identifiers':{'kobo': 'across-the-sea-of-suns-1'},
##                    'title':'Across the Sea of Suns', 'authors':['Gregory Benford']},
##                [title_test('Across the Sea of Suns',
##                    exact=True), authors_test(['Gregory Benford']),
##                    series_test('Galactic Centre', 2.0)]
##
##            ),

        ])
