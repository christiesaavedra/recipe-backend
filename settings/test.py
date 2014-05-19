DEBUG = False

DATABASES = {}
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# This should be set to the test domain (e.g. test.django-angular-pt.com)
ALLOWED_HOSTS = ['recipe.christinestephenson.me']

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4444444444444444444'

from base import *