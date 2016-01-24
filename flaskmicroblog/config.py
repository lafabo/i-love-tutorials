import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlight:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True         # WTForms deny cross-site query's for more security
SECRET_KEY = 'guess-what'       # token for WTForms CSRF

# List of OpenID providers
OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
	]

