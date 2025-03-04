'''
PRODUCTION SETTINGS

This import all the settings from the common which contain all settings for the 
old settings.py file that comes with django by default.
The aim of this file is to separate 'development' variable from production

'''


from .common import *

DEBUG = True

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware' ] #debug toolbar


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}