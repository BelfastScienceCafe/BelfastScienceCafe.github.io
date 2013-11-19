#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Belfast Science Cafe'
SITENAME = u'Belfast Science Cafe'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = (('Facebook', 'https://www.facebook.com/pages/Belfast-Science-Cafe/213056878715198?fref=ts'))

# Social widget
SOCIAL = ()#(('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/notmyidea'
INDEX_SAVE_AS = 'pages/news.html'
MENUITEMS = [('News', 'pages/news.html')]
