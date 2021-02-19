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
##from calibre.utils.icu import lower
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

#    def get_cached_cover_url(self, identifiers):
# I guess this routine returns an url that was discovered somewhere else and put into cache (how? where?)
#
# probably using cache_identifier_to_cover_url in the worket.py
# needs implementing... ISBN is the sole identifier
#
##        url = None
##        kobobooks_id = identifiers.get(self.ID_NAME, None)
##        if kobobooks_id is None:
##            isbn = identifiers.get('isbn', None)
##            if isbn is not None:
##                kobobooks_id = self.cached_isbn_to_identifier(isbn)
##        if kobobooks_id is not None:
##            url = self.cached_identifier_to_cover_url(kobobooks_id)
##        return url


##    def create_query(self, log, title=None, authors=None, identifiers={}):
##        log.info('entering create_query(self, log, title=None, authors=None, identifiers={})', log, title, authors, identifiers)
##        q = ''
##        isbn = check_isbn(identifiers.get('isbn', None))
##        if isbn is not None:
##            q = 'Query=%s&fcmedia=Book' % isbn
##        elif title:
##            log('create_query - title: "%s"'%(title))
##            title = get_udc().decode(title)
##            log('create_query - after decode title: "%s"'%(title))
##            tokens = []
##            title_tokens = list(self.get_title_tokens(title,
##                                strip_joiners=False, strip_subtitle=True))
##            log('create_query - title_tokens: "%s"'%(title_tokens))
##            author_tokens = self.get_author_tokens(authors, only_first_author=True)
##            tokens += title_tokens
##            tokens += author_tokens
##            tokens = [quote(t.encode('utf-8') if isinstance(t, unicode) else t) for t in tokens]
##            q = '+'.join(tokens)
##            q = 'Query=%s&fcmedia=Book'%q
##        if not q:
##            log.info('if not q return None')
##            return None
##        log.info("return '%s%s?%s&fclanguages=all'%(KoboBooks.BASE_URL, KoboBooks.SEARCH_PATH, q)", '%s%s?%s&fclanguages=all'%(KoboBooks.BASE_URL, KoboBooks.SEARCH_PATH, q))
##        return '%s%s?%s&fclanguages=all'%(KoboBooks.BASE_URL, KoboBooks.SEARCH_PATH, q)
##

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
        if debug: log.info(soup.prettify())

        return soup

    def verify_isbn(self, log, isbn_str):
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
        if debug:
            log.info("\nIn verify_isbn(isbn_str)")
            log.info("isbn_str         : ",isbn_str)

        total=0

        for k in ['(',')','-',' ']:
            if k in isbn_str:
                isbn_str=isbn_str.replace(k,"")
        if debug:
            log.info("isbn_str cleaned : ",isbn_str)
           

        return check_isbn(isbn_str)         # calibre does the check for me after cleaning... 

    def req_mtd_post(self, log, rkt, ModeMoteur="LITTERAL"):
        # Accède en mode post sur <base_url>/livres/noosearch.asp
        # Access using "post" method over <base_url>/livres/noosearch.asp
        #
        debug=1
        if debug: log.info("\nIn req_mtd_post(rkt)")

        search_urn="https://www.noosfere.org/livres/noosearch.asp"
        base_rkt={"ModeMoteur":ModeMoteur,"ModeRecherche":"AND","recherche":"1","Envoyer":"Envoyer"}

        rkt.update(base_rkt)
        if debug: log.info("rkt",rkt)
        req=urllib.parse.urlencode(rkt).encode('ascii')
        try: sr=urllib.request.urlopen(search_urn,req,timeout=30)
        except TimeoutError:
            log.info("A network timeout occurred, do you have wide world web access?")
            sys.exit("désolé")
        except urllib.error.HTTPError as e:
            log.info("Une erreur envoyée par le site a été reçue.")
            log.info("code : ",e.code,"reason : ",e.reason)
            sys.exit("réponse d'erreur de l'url, désolé")
        except urllib.error.URLError as e:
            log.info("Une erreur envoyée par le site a été reçue.")
            log.info("reason : ",e.reason)
            sys.exit("réponse d'erreur de l'url, désolé")
        if debug:
            log.info("type(sr) : ",type(sr))
            log.info("sr.header\n")
            for i in sr.headers:
                    log.info(i, " : ",sr.headers[i])

        soup = self.make_soup(log, sr)
        return soup

    def ISBN_ret_book_index(self, log, soup):
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

        book_index={}

        tmp_rbi=soup.select('a[href*="editionsLivre.asp"]')
        if len(tmp_rbi):
            for i in range(len(tmp_rbi)):
                if debug:
                    log.info("tmp_rbi["+str(i)+"].text, tmp_rbi["+str(i)+"]['href'] : ",tmp_rbi[i].text,tmp_rbi[i]["href"])
                book_index[tmp_rbi[i].text]=(tmp_rbi[i]["href"])

        return book_index

# this is the entry point...
    def identify(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
        log.info('\nEntering identify(self, log, result_queue, abort, title=None, authors=None,identifiers={}, timeout=30)')
        log.info('log          : ', log)
        log.info('result_queue : ', result_queue)
        log.info('abort        : ', abort)
        log.info('title        : ', title)
        log.info('authors      : ', authors, type(authors))
        log.info('identifiers  : ', identifiers)
        log.info('\n')

        '''
        Note this method will retry without identifiers automatically if no
        match is found with identifiers.
        '''
        debug=1
        
        isbn = self.verify_isbn(log, identifiers.get('isbn', None))

        for i in range(len(authors)):                   # authors needs to be cleaned to produce correct results
            for k in [',','.','-']:
                if k in authors[i]:
                    authors[i] = authors[i].replace(k," ")
        if debug: log.info('authors cleaned : ',authors)
        

        if isbn:
            rkt = {"Mots": isbn,"livres":"livres"}
            soup = self.req_mtd_post(log, rkt, ModeMoteur="MOTS-CLEFS")        #if isbn valid then we want to select exact match ("correspondance exacte")
            book_index = self.ISBN_ret_book_index(log, soup)
            if not len(book_index):
                log.info("This ISBN : ", isbn, "was not found.")
                sys.exit("Sorry.")
            else:
                for key,ref in book_index.items():
                    livrel,indexl = key,ref
                if debug: log.info("livrel : ",livrel,"url : ",indexl)
##        elif authors:
                

        sys.exit("on sort ici...")

##        matches = []        # list of matches (url,publisher)
##        log('identify - title: "%s" authors= "%s"'%(title, authors))
##
##        # If we have a KoboBooks id then we do not need to fire a "search".
##        # Instead we will go straight to the URL for that book.
##        kobobooks_id = identifiers.get(self.ID_NAME, None)
##        br = self.browser
##        if kobobooks_id:
##            matches.append(('%s%s%s'%(KoboBooks.BASE_URL, KoboBooks.BOOK_PATH, kobobooks_id), None))
###            log("identify - kobobooks_id=", kobobooks_id)
###            log("identify - matches[0]=", matches[0])
##        else:
##            query = self.create_query(log, title=title, authors=authors, identifiers=identifiers)
##            if query is None:
##                log.error('Insufficient metadata to construct query')
##                return
##            try:
##                log.info('Querying: %s'%query)
###                 br.set_handle_redirect(True)
##                raw = br.open_novisit(query, timeout=timeout).read()
###                 raw = br.open(query, timeout=timeout).read()
###                 open('E:\\t.html', 'wb').write(raw)
##            except Exception as e:
##                err = 'Failed to make identify query: %r'%query
##                log.exception(err)
##                return as_unicode(e)
##            root = fromstring(clean_ascii_chars(raw))
##            # Now grab the match from the search result, provided the
##            # title appears to be for the same book
##            self._parse_search_results(log, title, root, matches, timeout)

        if abort.is_set():
            return
##
##        if not matches:
##            if identifiers and title and authors:
##                log('No matches found with identifiers, retrying using only'
##                        ' title and authors. Query: %r'%query)
##                return self.identify(log, result_queue, abort, title=title,
##                        authors=authors, timeout=timeout)
##            log.error('No matches found with query: %r'%query)
##            return



##        from calibre_plugins.kobobooks.worker import Worker
##        author_tokens = list(self.get_author_tokens(authors))
##        workers = [Worker(data[0], data[1], author_tokens, result_queue, br, log, i, self.category_handling, self) for i, data in
##                enumerate(matches)]
##
##        for w in workers:
##            w.start()
##            # Don't send all requests at the same time
##            time.sleep(0.1)
##
##        while not abort.is_set():
##            a_worker_is_alive = False
##            for w in workers:
##                w.join(0.2)
##                if abort.is_set():
##                    break
##                if w.is_alive():
##                    a_worker_is_alive = True
##            if not a_worker_is_alive:
##                break
##
##        return None


# this is local method
#
##    def _parse_search_results(self, log, orig_title, root, matches, timeout):
##        log.info('entering _parse_search_results(self, log, orig_title, root, matches, timeout)', self, log, orig_title, root, matches, timeout)
##
##        def ismatch(title):
##            title = lower(title)
##            match = not title_tokens
##            for t in title_tokens:
##                if lower(t) in title:
##                    match = True
##                    break
##            return match
##
##        title_tokens = list(self.get_title_tokens(orig_title))
##        max_results = 5
##        for data in root.xpath('//div[@class="SearchResultsWidget"]/section/div/ul/li'):
##            log.error('data: %s' % (tostring(data)))
##            try:    # Seem to be getting two different search results pages. Try the most ccmmon first.
##                item_info = data.xpath('./div/div/div[@class="item-info"]')[0]
##                log.error('used three divs item_info')
##            except:
##                log.error('failed using three divs')
##                item_info = data.xpath('./div/div[@class="item-info"]')[0]
###             log.error('item_info: ', item_info)
###            log.error("item_info.xpath('./p/a/@href'): %s" % (item_info.xpath('./p/a/@href')))
###            log.error("item_info.xpath('./p/a/@href')[0]: %s" % (tostring(item_info.xpath('./p/a/@href')[0])))
##            title_ref = item_info.xpath('./p/a')[0]
##            log.error("title_ref: ", tostring(title_ref))
##            kobobooks_id = title_ref.xpath('./@href')[0]
##            log.error("kobobooks_id: ", kobobooks_id)
##            kobobooks_id = kobobooks_id.split('/')
##            log.error("kobobooks_id: ", kobobooks_id)
##            kobobooks_id = kobobooks_id[-1].strip()
##            log.error("kobobooks_id: '%s'" % (kobobooks_id))
##            kobobooks_id = kobobooks_id[len(kobobooks_id) - 1]
##            log.error("kobobooks_id: ", kobobooks_id)
##            log('_parse_search_results - kobobooks_id: %s'%(kobobooks_id))
##            if not id:
##                continue
##
###            log.error('data: %s'%(tostring(data.xpath('./a'))))
###            log.error('data: %s'%(tostring(data.xpath('./a/p'))))
###            log.error('data: %s'%(data.xpath('./a/p/span/text()')))
##            title = title_ref.text
##            log.error("title: '%s'" % (title))
##            if not ismatch(title):
##                log.error('Rejecting as not close enough match: %s'%(title))
##                continue
##            log.error("Have close enough match - title='%s', id='%s'" % (title, kobobooks_id))
##            publisher = ''#.join(data.xpath('./li/a/a/text()'))
##            url = '%s%s%s'%(KoboBooks.BASE_URL, KoboBooks.BOOK_PATH, kobobooks_id)
##            matches.append((url, publisher))
##            if len(matches) >= max_results:
##                break

######################################### not tested ################################
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
