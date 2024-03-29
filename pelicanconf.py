#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SP-SUM, DLR e.V. Dresden'
SITENAME = 'Adaptable Poly-Engineering Simulator'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theming with m.css:
#THEME = 'm.css/pelican-theme'
THEME = 'sts-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_FAVICON = ('/static/favicon.ico', 'image/x-ico')
M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Libre+Baskerville:400,400i,700,700i%7CSource+Code+Pro:400,400i,600',
               '/static/m-light.css']
M_THEME_COLOR = '#cb4b16'
#M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
#               '/static/m-dark.css']
#M_THEME_COLOR = '#22272e'
M_FINE_PRINT = '''
Mainly developed by `SP of DLR e.V. <https://www.dlr.de/content/en/institutes/institute-of-software-methods-for-product-virtualization.html>`_ in Dresden,
this page is generated with `pelican <https://getpelican.com>`_
and uses `m.css <https://mcss.mosra.cz>`_,
hosted on `OSDN <https://osdn.net>`_.
`Impressum <impressum>`_ und `Datenschutz <datenschutz>`_.
'''
M_SITE_LOGO = '/images/apes_logo.png'
M_SITE_LOGO_TEXT = ''
M_LINKS_NAVBAR1 = [('Ateles', '/pages/ateles', 'ateles', []),
                   ('Musubi', '/pages/musubi', 'musubi', []),
                   ('Seeder', '/pages/seeder', 'seeder', []),
                   ('Treelm', '/pages/treelm', 'treelm', []),
                   ('Aotus',  '/pages/aotus',  'aotus',  []),
                   ('Impressum',  '/pages/impressum',  'impressum',  []),
                   ('Datenschutz',  '/pages/datenschutz',  'datenschutz',  [])]

PLUGIN_PATHS = ['m.css/plugins/m']
PLUGINS = ['htmlsanity', 'images']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
