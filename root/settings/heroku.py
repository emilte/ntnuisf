import os
import django_heroku

from root.constants import Environment
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

# ALLOWED_HOSTS = ['my-app.herokuapp.com']

# Values are set in heroku dashboard
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = eval(os.environ['DEBUG'])  # pylint: disable=eval-used

# Ensure correct ENV
ENV = Environment.HEROKU

#  Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

# activate django-heroku.
django_heroku.settings(locals())
