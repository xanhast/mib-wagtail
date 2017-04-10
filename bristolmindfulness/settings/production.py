from __future__ import absolute_import, unicode_literals

from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bristolmindfulness_db',
    }
}


try:
    from .local import *
except ImportError:
    pass
