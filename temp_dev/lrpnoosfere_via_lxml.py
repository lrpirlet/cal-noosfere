#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2021, Louis Richard Pirlet'
__docformat__ = 'restructuredtext en'

from bs4 import BeautifulSoup as BS
import socket, datetime
from threading import Thread
import urllib
from lxml import etree as et
from lxml.html import fromstring, tostring

##from calibre.ebooks.metadata.book.base import Metadata
##from calibre.ebooks.metadata import check_isbn
### from calibre.library.comments import sanitize_comments_html
##from calibre.utils.cleantext import clean_ascii_chars
##from calibre.utils.icu import lower
##
import sys
import mechanize
br = mechanize.Browser()

def load_url(log, url, br):           # url is builded url, br is either browser or cloned-browser
    try:
        log.info('Querying: %s' % query)
        response = br.open(str(query))
    except Exception as e:
        log.exception(e)
        raise Exception('Failed to make identify query: %r - %s ' % (query,e))
            
    try:
        raw = response.read().strip()
        if not raw:
            log.error('Failed to get raw result for query: %r'%query)
            raise Exception('Failed to get raw result for query: %r'%query)
        root = fromstring(clean_ascii_chars(raw))
    except:
        msg = 'Failed to parse martinussk page for query: %r'%query
        log.exception(msg)
        raise Exception(msg)
    return root

###
from lxml import etree as et                            # ea pour construire vol_comment soup
from lxml.builder import E
debug=1
url="https://www.noosfere.org/livres/niourf.asp?numlivre=-323150&Tri=3"
from_encoding = "windows-1252"
who=">>"
sr=urllib.request.urlopen(url,timeout=30)
r = sr.read().strip()                                   # get response as a byte stream encoded in windows-1252
rdu = r.decode(from_encoding).encode("utf-8")           # response is now a byte stream encoded in utf-8
###
##        sr=br.open(vol_url,timeout=20)
url_vrai=sr.geturl()
if debug:
    print(who,"sr.info()     :\n", sr.info())
    print(who,"ha ouais, vraiment? charset=iso-8859-1... c'est pas vrai, c'est du", from_encoding,"...")
    print(who,"# isolé pour trouver quel est l'encodage d'origine... ça marchait à peu pres sans forcer encodage d'entrée mais pas tout a fait")
    print(who,"# il n'est pas improbable que ce soit ça que le site va modifier dans le futur...")
    print(who,"#")
    print(who,'# variable "from_encoding" isolated to find out what is the site character encoding... The announced charset is WRONG')
    print(who,"# requests was able to decode correctly, I knew that my setup was wrong but it took me a while...")
    print(who,"# Maybe I should have tried earlier the working solution as the emitting node is MS")
    print(who,"# (Thanks MS!!! and I mean it as I am running W10.. :-) but hell, proprietary standard is not standard)...")
    print(who,"# It decode correctly to utf_8 with windows-1252 forced as from_encoding")
    print(who,"# watch-out noosfere is talking about making the site better... ;-}")
    print(who,"#'")
    print(who,"sr.getcode()  : ",sr.getcode())
    print(who,"url_vrai      : ",url_vrai)

    soup = BS(sr, "html5lib",from_encoding=from_encoding)
#        if debug: print(who,soup.prettify())              # useful but too big...

tmp_lst=[]
vol_info={}
vol_title=vol_auteur=vol_auteur_prenom=vol_auteur_nom=vol_serie=vol_serie_seq=vol_editor=vol_coll=vol_coll_nbr=vol_dp_lgl=vol_isbn=vol_genre=vol_cover_index=""
comment_generic=comment_resume=comment_Critique=comment_Sommaire=comment_AutresCritique=comment_cover=None

##vol_comment_soup=BS('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>',"html5lib")
##if debug: print(who,"vol reference found")
vol_comment=et.Element("html")
vol_comment.append(et.Element("head"))
vol_comment.append(et.fromstring('<div><p>Référence: <a href="' + url_vrai + '">' + url_vrai + '</a></p></div>'))

print(type(vol_comment))

a=(et.tostring(vol_comment, pretty_print=True)).decode("utf-8")
print(a)

sys.exit("stop here")

if soup.select("span[class='TitreNiourf']"): vol_title = soup.select("span[class='TitreNiourf']")[0].text.strip()
if debug: print(who,"vol_title found")

if soup.select("span[class='AuteurNiourf']"): vol_auteur = soup.select("span[class='AuteurNiourf']")[0].text.replace("\n","").strip()
if debug: print(who,"vol_auteur found")
for i in range(len(vol_auteur.split())):
    if not vol_auteur.split()[i].isupper():
        vol_auteur_prenom += " "+vol_auteur.split()[i]
    else:
        vol_auteur_nom += " "+vol_auteur.split()[i].title()
vol_auteur = vol_auteur.title()
vol_auteur_prenom = vol_auteur_prenom.strip()
if debug: print(who,"vol_auteur_prenom found")
vol_auteur_nom = vol_auteur_nom.strip()
if debug: print(who,"vol_auteur_nom found")

if soup.select("a[href*='serie.asp']"):
    vol_serie = soup.select("a[href*='serie.asp']")[0].text
    tmp_vss = [x for x in soup.select("a[href*='serie.asp']")[0].parent.stripped_strings]
    for i in range(len(tmp_vss)):
        if "vol." in tmp_vss[i]:
            vol_serie_seq=tmp_vss[i].replace("vol.","").strip()
if debug: print(who,"vol_serie, vol_serie_seq found")

comment_generic = soup.select("span[class='ficheNiourf']")[0]
new_div=soup.new_tag('div')
comment_generic = comment_generic.wrap(new_div)
if debug: print(who,"comment_generic found")

if soup.select("a[href*='editeur.asp']"): vol_editor = soup.select("a[href*='editeur.asp']")[0].text
if debug: print(who,"vol_editor found")

if soup.select("a[href*='collection.asp']"): vol_coll = soup.select("a[href*='collection.asp']")[0].text
if debug: print(who,"vol_coll")

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
if debug: print(who,"vol_coll_nbr found")

for elemnt in soup.select("span[class='sousFicheNiourf']")[0].stripped_strings:
    if "Dépôt légal" in elemnt:
        elemnt = elemnt.replace("Dépôt légal :","").strip()
    if len(str(vol_dp_lgl))<3:
        if "trimestre" in elemnt:
            print(who,"*************vol_dp_lg bizare*************do some*************",elemnt)
            ele=elemnt.split()
            vol_dp_lgl=datetime.datetime.strptime(("000"+str((int(ele[0][0])-1)*91+47))[-3:]+" "+ele[2],"%j %Y")
        for i in ("janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"):
            if i in elemnt:
                vol_dp_lgl=elemnt
                vol_dp_lgl=datetime.datetime.strptime(vol_dp_lgl,"%B %Y")
                break
    if "ISBN" in elemnt:
        vol_isbn = elemnt.lower().replace(" ","").replace('isbn:','')
        if "néant" in vol_isbn: vol_isbn=""
        if debug: print(who,"vol_isbn found")
    if "Genre" in elemnt: vol_genre = elemnt.lstrip("Genre : ")
if debug: print(who,"vol_dp_lgl, vol_isbn, vol_genre found")

if soup.select("img[name='couverture']"):
    for elemnt in repr(soup.select("img[name='couverture']")[0]).split('"'):
        if "http" in elemnt:
            if not vol_cover_index:
                vol_cover_index = elemnt
                if debug: print(who,"vol_cover_index found")

if vol_cover_index:
    comment_cover = BS('<div><p>Couverture: <a href="' + vol_cover_index + '">Link to image </a></p></div>',"html5lib")

# select the fields I want... More exist such as film adaptations or references to advises to read
# but that is not quite consistant around all the books (noosfere is a common database from many people)
# and beside I have enough info like that AND I do NOT want to take out the noosfere's business

tmp_comm_lst=soup.select("td[class='onglet_biblio1']")
#        if debug: print(who,tmp_comm_lst)             #usefull but too long
for i in range(len(tmp_comm_lst)):
    if "Quatrième de couverture" in str(tmp_comm_lst[i]):
        comment_pre_resume = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Quatrième de couverture</p></div>',"html5lib")
        comment_resume = soup.select("div[id='Résumes']")[0]
        if debug: print(who,"comment_resume found")

    if "Critique" in str(tmp_comm_lst[i]):
        if not "autres" in str(tmp_comm_lst[i]):
            comment_pre_Critique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques</p></div>',"html5lib")
            comment_Critique = soup.select("div[id='Critique']")[0]
            if debug: print(who,"comment_Critique found")

    if "Sommaire" in str(tmp_comm_lst[i]):
        comment_pre_Sommaire = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Sommaire</p></div>',"html5lib")
        comment_Sommaire = soup.select("div[id='Sommaire']")[0]
        if debug: print(who,"comment_Sommaire found")

    if "Critiques des autres" in str(tmp_comm_lst[i]):
        comment_pre_AutresCritique = BS('<div><p> </p><p align="center" style="font-weight: 600; font-size: 18px">Critiques des autres éditions ou de la série</p></div>',"html5lib")
        comment_AutresCritique = soup.select("div[id='AutresCritique']")[0]
        if debug: print(who,"comment_AutresCritique found")
        if comment_AutresCritique.select('a[href*="serie.asp"]'):
            critic_url = "https://www.noosfere.org/livres/"+comment_AutresCritique.select('a[href*="serie.asp"]')[0]['href']
            try:
                comment_AutresCritique=get_Critique_de_la_serie(critic_url)
            except:
                log.exception("get_Critique_de_la_serie failed for url: ",critic_url)

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
    print(who,"+"*50)
#    print(who,"lrpid, type()                  : ",lrpid, type(lrpid))                    # must be <class 'str'>
#    print(who,"relevance, type()              : ",relevance, type(relevance))            # must be <class 'float'>
    print(who,"vol_title, type()              : ",vol_title, type(vol_title))                      # must be <class 'str'>
    print(who,"vol_auteur, type()             : ",vol_auteur, type(vol_auteur))                    # must be <class 'list'> of <class 'str'>
    print(who,"vol_auteur_prenom, type()      : ",vol_auteur_prenom, type(vol_auteur_prenom))      # must be <class 'str'>
    print(who,"vol_auteur_nom, type()         : ",vol_auteur_nom, type(vol_auteur_nom))            # must be <class 'str'>
    print(who,"vol_serie, type()              : ",vol_serie, type(vol_serie))                      # must be <class 'str'>
    print(who,"vol_serie_seq, type()          : ",vol_serie_seq, type(vol_serie_seq))              # must be <class 'float'>
    print(who,"vol_editor, type()             : ",vol_editor, type(vol_editor))                    # must be <class 'str'>
    print(who,"vol_coll, type()               : ",vol_coll, type(vol_coll))                        # must be
    print(who,"vol_coll_nbr, type()           : ",vol_coll_nbr, type(vol_coll_nbr))                # must be
    print(who,"vol_dp_lgl, type()             : ",vol_dp_lgl, type(vol_dp_lgl))                    # must be <class 'datetime.datetime'> ('renderer=isoformat')
    print(who,"vol_isbn, type()               : ",vol_isbn, type(vol_isbn))                        # must be <class 'str'>
    print(who,"vol_genre, type()              : ",vol_genre, type(vol_genre))                      # must be <class 'list'> of <class 'str'>
    print(who,"vol_cover_index, type()        : ",vol_cover_index, type(vol_cover_index))          # must be
    print(who,"type(vol_comment_soup)         : ",type(vol_comment_soup))                         # must be byte encoded (start with b'blablabla...
    print(who,"vol_comment_soup               :\n",vol_comment_soup)                                # Maybe a bit long sometimes
                                                                                                       # language must be <class 'str'>
                                                                                                        # rating  must be <class 'str'>
    print(who,"="*50)

##
##
##    if vol_isbn and vol_cover_index:
##            plugin.cache_isbn_to_identifier(vol_isbn, lrpid)
##    plugin.cache_identifier_to_cover_url(lrpid, vol_cover_index)
##
##        mi = Metadata(vol_title, [vol_auteur])
##        mi.set_identifier('lrpid', lrpid)
##        if mi.pubdate:
##            pubdate = vol_dp_lgl                         #<==  'str' object has no attribute 'isoformat'
##        mi.publisher = vol_editor
##        mi.isbn = vol_isbn
##        if vol_serie:
##            mi.series = vol_serie
##            mi.series_index = float(vol_serie_seq)
##        mi.tags = [vol_genre]
##        mi.rating = float(0)
##        
###        comments = tostring(description_node, method='html') from kobobook
##
###        mi.comments = vol_comment_soup.encode()               # original that failed... needs to be byte encoded b'blablabla
##
##        tmp_comments = vol_comment_soup.encode('utf-8')
##        print("\n"*3, type(tmp_comments),"\n",tmp_comments)
##
##        root = fromstring(tmp_comments)
##        print("\n"*3, type(root),"\n",root,"\n")
##       
##        mi.comments = tostring(root, method='html')              # needs to be lxml byte encoded b'blablabla
##        mi.language = "fra"
##        mi.source_relevance = relevance
##        mi.has_cover = bool(vol_cover_index)
##
##        print(who,"mi\n",mi,"\n")
##
##        plugin.clean_downloaded_metadata(mi)
##
##        result_queue.put(mi)
##
##
##
##        mi = Metadata(title, authors)
##        mi.set_identifier('kobo', kobobooks_id)
##        kobobooks_id = kobobooks_id
##
##        # Some of the metadata is in a JSON object in script tag.
##        try:
##            import json
##            scripts = root.xpath('//div[@data-kobo-widget="RatingAndReviewWidget"]/script')
##            if len(scripts) > 0:
##                json_details = scripts[1].text
##                if json_details is not None:
##                    page_metadata = json.loads(json_details, strict=False)
##                    log("Script page_metadata=", page_metadata)
###                     log("Script page_metadata keys=", page_metadata.keys())
##                    try:
##                        pubdate = page_metadata["releasedate"]
##                        pubdate = datetime.datetime.strptime(pubdate, "%Y-%m-%dT%H:%M:%S")
##                        mi.pubdate = pubdate
##                        log("pubdate from JSON:", mi.pubdate)
##                    except:
##                        log.exception('Error parsing page for pubdate: url=%r'%url)
##
##                    try:
##                        mi.publisher = page_metadata["brand"]
##                    except:
##                        log.exception('Error parsing page for publisher: url=%r'%url)
##
##                    try:
##                        isbn = page_metadata["gtin13"]
##                        if isbn:
##                            isbn = mi.isbn = isbn
##                    except:
##                        log.exception('Error parsing ISBN for url: %r'%url)
##
##            else:
##                log("No scripts founds for book details metadata????")
##        except Exception as e:
##            log("Exception thrown getting scripts:", e)
##
##
##        try:
##            (mi.series, mi.series_index) = parse_series(root)
##        except:
##            log.exception('Error parsing series for url: %r'%url)
##
##        try:
##            mi.tags = parse_tags(root)
##        except:
##            log.exception('Error parsing tags for url: %r'%url)
##
##        try:
##            mi.rating = parse_rating(root)
##        except:
##            log.exception('Error parsing ratings for url: %r'%url)
##
##        try:
##            cover_url = parse_cover(root)
##        except:
##            log.exception('Error parsing cover for url: %r'%url)
##        mi.has_cover = bool(cover_url)
##
##        try:
##            mi.comments = parse_comments(root)
##        except:
##            log.exception('Error parsing comments for url: %r'%url)
##
##        try:
##            language = parse_language(root)
##            if language:
##                lang = mi.language = language
##        except:
##            log.exception('Error parsing languages for url: %r'%url)
##
##        mi.source_relevance = relevance
##
##        if kobobooks_id:
##            if cover_url:
##                plugin.cache_identifier_to_cover_url(kobobooks_id, cover_url)
##
##        plugin.clean_downloaded_metadata(mi)
##
##        result_queue.put(mi)


##
##    def _get_metadata(self, book_id, get_user_categories=True):  # {{{
##        mi = Metadata(None, template_cache=formatter_template_cache)
##
##        mi._proxy_metadata = ProxyMetadata(self, book_id, formatter=mi.formatter)
##
##        author_ids = _field_ids_for('authors', book_id)
##        adata = _author_data(author_ids)
##        aut_list = [adata[i] for i in author_ids]
##        aum = []
##        aus = {}
##        aul = {}
##        for rec in aut_list:
##            aut = rec['name']
##            aum.append(aut)
##            aus[aut] = rec['sort']
##            aul[aut] = rec['link']
##        mi.title       = _field_for('title', book_id,
##                default_value=_('Unknown'))
##        mi.authors     = aum
##        mi.author_sort = _field_for('author_sort', book_id,
##                default_value=_('Unknown'))
##        mi.author_sort_map = aus
##        mi.author_link_map = aul
##        mi.comments    = _field_for('comments', book_id)
##        mi.publisher   = _field_for('publisher', book_id)
##        n = utcnow()
##        mi.timestamp   = _field_for('timestamp', book_id, default_value=n)
##        mi.pubdate     = _field_for('pubdate', book_id, default_value=n)
##        mi.uuid        = _field_for('uuid', book_id,
##                default_value='dummy')
##        mi.title_sort  = _field_for('sort', book_id,
##                default_value=_('Unknown'))
##        mi.last_modified = _field_for('last_modified', book_id,
##                default_value=n)
##        formats = _field_for('formats', book_id)
##        mi.format_metadata = {}
##        mi.languages = list(_field_for('languages', book_id))
##        if not formats:
##            good_formats = None
##        else:
##            mi.format_metadata = FormatMetadata(self, book_id, formats)
##            good_formats = FormatsList(sorted(formats), mi.format_metadata)
##        # These three attributes are returned by the db2 get_metadata(),
##        # however, we dont actually use them anywhere other than templates, so
##        # they have been removed, to avoid unnecessary overhead. The templates
##        # all use _proxy_metadata.
##        # mi.book_size   = _field_for('size', book_id, default_value=0)
##        # mi.ondevice_col = _field_for('ondevice', book_id, default_value='')
##        # mi.db_approx_formats = formats
##        mi.formats = good_formats
##        mi.has_cover = _('Yes') if _field_for('cover', book_id,
##                default_value=False) else ''
##        mi.tags = list(_field_for('tags', book_id, default_value=()))
##        mi.series = _field_for('series', book_id)
##        if mi.series:
##            mi.series_index = _field_for('series_index', book_id,
##                    default_value=1.0)
##        mi.rating = _field_for('rating', book_id)
##        mi.set_identifiers(_field_for('identifiers', book_id,
##            default_value={}))
##        mi.application_id = book_id
##        mi.id = book_id
##        composites = []
##        for key, meta in field_metadata.custom_iteritems():
##            mi.set_user_metadata(key, meta)
##            if meta['datatype'] == 'composite':
##                composites.append(key)
##            else:
##                val = _field_for(key, book_id)
##                if isinstance(val, tuple):
##                    val = list(val)
##                extra = _field_for(key+'_index', book_id)
##                mi.set(key, val=val, extra=extra)
##        for key in composites:
##            mi.set(key, val=_composite_for(key, book_id, mi))
##
##        user_cat_vals = {}
##        if get_user_categories:
##            user_cats = backend.prefs['user_categories']
##            for ucat in user_cats:
##                res = []
##                for name,cat,ign in user_cats[ucat]:
##                    v = mi.get(cat, None)
##                    if isinstance(v, list):
##                        if name in v:
##                            res.append([name,cat])
##                    elif name == v:
##                        res.append([name,cat])
##                user_cat_vals[ucat] = res
##        mi.user_categories = user_cat_vals
##
##        return mi
##    # }}}
