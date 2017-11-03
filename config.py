WTF_CSRF_ENABLED = True
SECRET_KEY = 's0m3-r@nd0m-s3cr3t-k3y'

OPENID_PROVIDERS = [
    {'name':'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo', 'url':'https://me.yahoo.com'},
    {'name':'AOL', 'url':'http://openid.aol.com/<username>'},
    {'name':'Flickr', 'url':'http://www.flickr.com/<username>'},
    {'name':'MyOpenID', 'url': 'https://www.myopenid.com'}
]
