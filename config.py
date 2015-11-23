import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://accounts.google.com/login#identifier'},
    {'name': 'Yahoo', 'url': 'https://www.yahoo.com/'},
    {'name': 'AOL', 'url': 'https://www.openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'https://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.openid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
