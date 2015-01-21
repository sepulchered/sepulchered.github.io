#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sepulchered'
SITENAME = 'sepulchered'
SITEURL = 'http://andrey.dresvyannikov.ru'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
THEME = 'pelican-svbhack'
USER_LOGO_URL = SITEURL + '/static/img/ava.jpg'
GOOGLE_ANALYTICS = "UA-38597125-3"
DISQUS_SITENAME = 'andreydresvyannikovru'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', '/about.html'),
         ('CV', '/cv.html'),)

# Social widget
SOCIAL = (('github', 'https://github.com/sepulchered'),
          ('twitter', 'https://twitter.com/dresvyannikov_a'),
          ('linkedin', 'ru.linkedin.com/in/sepulchered'),
          ('facebook', 'https://www.facebook.com/dresvyannikov.a'),
         )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
