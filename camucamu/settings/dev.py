from camucamu.settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, 'camucamu.db'),  # Or path to database file if using sqlite3.
    }
}

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'camucamu.wsgi.dev.application'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
