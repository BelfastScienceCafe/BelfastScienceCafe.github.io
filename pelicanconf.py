#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General Info
AUTHOR = u'Belfast Science Cafe'
SITENAME = u'Belfast Science Cafe'
SITEURL = ''
TIMEZONE = 'Europe/Belfast'
DEFAULT_LANG = u'en'


# Blogroll


## Visuals
THEME = 'themes/notmyidea'
# Social widget (links on page)
SOCIAL = (('Facebook', 'https://www.facebook.com/pages/Belfast-Science-Cafe/213056878715198?fref=ts'),
         ('British Science Association', 'http://www.britishscienceassociation.org/'),)
# Menus
MENUITEMS = [('Home', '/index.html'), ('Events', '/events.html')]
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['liquid_tags.img']



#~ SITE_URL = 'http://belfastsciencecafe.github.io'
#~ RELATIVE_URLS = False

# Paths
ARTICLE_URL = 'events/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'events/{date:%Y}/{slug}/index.html'
STATIC_PATHS = ['images', 'files']
INDEX_SAVE_AS = 'events.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5
