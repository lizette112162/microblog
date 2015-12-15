import os
basedir = os.path.abspath(os.path.dirname(__file__))

# microsft translation service
# -*- coding: utf-8 -*-

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
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
MAIL_PORT = os.environ.get('MAIL_PORT', 465)
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = True
# administrator list
ADMINS = os.environ.get('ADMINS', '').split(',')

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

#!/usr/bin/env python
# ...
# available languages
LANGUAGES = {
        'en': 'English',
        'es': 'Espanol'
 }

MS_TRANSLATOR_CLIENT_ID =  os.environ.get('MS_TRANSLATOR_CLIENT_ID')
MS_TRANSLATOR_CLIENT_SECRET = os.environ.get('MS_TRANSLATOR_CLIENT_SECRET')

