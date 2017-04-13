from __future__ import absolute_import, unicode_literals

from .base import *

import os

ALLOWED_HOSTS = ['127.0.0.1', 'bristolmindfulness.com', 'www.bristolmindfulness.com', os.environ['VDT_DOMAIN']]

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
MEDIA_URL = '/media'


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['VDT_DB_NAME'],
        'USER': os.environ['VDT_DB_USER'],
        'PASSWORD': os.environ['VDT_DB_PASS'],
        'HOST': os.environ['VDT_DB_HOST'],
        'PORT': '5432',
    }
}


try:
    from .local import *
except ImportError:
    pass
