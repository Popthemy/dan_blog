'''
DEVELOPMENT SETTINGS

This import all the settings from the common which contain all settings for the 
old settings.py file that comes with django by default.
The aim of this file is to separate 'production' variable from development

'''
import dj_database_url
from .common import *
from decouple import config

DEBUG = config('debug',default=False, cast=bool)

ALLOWED_HOSTS = ['dan-blog.onrender.com']

DJANGO_SETTINGS_MODULE = 'dan_diary.settings.prod'


DATABASES = {
    'default': dj_database_url.parse(config('DB_URL'))
}