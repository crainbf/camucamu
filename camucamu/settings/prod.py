from camucamu.settings.common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'camucamu.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'camucamu.wsgi.prod.application'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'camucamuapp@gmail.com'
EMAIL_HOST_PASSWORD = 'Markus10'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True

TEMPLATE_DEBUG = DEBUG
