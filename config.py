WTF_CSRF_ENABLED = True
SECRET_KEY = 's0m3-r@nd0m-s3cr3t-k3y'

OPENID_PROVIDERS = [
    {'name':'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo', 'url':'https://me.yahoo.com'},
    {'name':'AOL', 'url':'http://openid.aol.com/<username>'},
    {'name':'Flickr', 'url':'http://www.flickr.com/<username>'},
    {'name':'MyOpenID', 'url': 'https://www.myopenid.com'}
]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# mail settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# admin list
ADMINS = ['dev@localhost']

# pagination
POSTS_PER_PAGE = 3

# search
WHOOSH_BASE = os.path.join(basedir, 'search_index')
MAX_SEARCH_RESULTS = 10
