from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_x&pc60_3(4099z#kwm51@yag%09=6l27q!kof=s+4=60pj9(_'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'bristolmindfulness_db',
    }
}

ALLOWED_HOSTS = ['0.0.0.0', 'mib-wagtail-xanhast.c9users.io']

try:
    from .local import *
except ImportError:
    pass
