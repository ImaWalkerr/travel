import os

from .config import *


SECRET_KEY = os.getenv('DJANGO_DEVELOPMENT_SECRET_KEY')

ALLOWED_HOSTS = os.getenv('DEVELOPMENT_ALLOWED_HOSTS').split(',')

INTERNAL_IPS = os.getenv('DEBUG_HOSTS').split(',')

INSTALLED_APPS += ['debug_toolbar']

DEBUG = True

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

