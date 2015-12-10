import os
basedir = os.path.abspath(os.path.dirname(__file__))

# microsft translation service

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
        {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
        {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
        {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# email server
MAIL_SERVER = 'localhost'
MAIL_PORT =  25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ...
# available languages
LANGUAGES = {
        'en': 'English',
        'es': 'Espanol'
 }

MS_TRANSLATOR_CLIENT_ID = 'micro-blog'
MS_TRANSLATOR_CLIENT_SECRET = 'bbvcxLR5IbDalpmivYE8OQ6PR/uo4Bi8XATpp7AnER8='

