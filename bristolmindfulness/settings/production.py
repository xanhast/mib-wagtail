from __future__ import absolute_import, unicode_literals

from .base import *

import os

ALLOWED_HOSTS = ['127.0.0.1', 'bristolmindfulness.com', 'www.bristolmindfulness.com', os.environ['VDT_DOMAIN']]

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/'

AWS_STORAGE_BUCKET_NAME = env['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

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
