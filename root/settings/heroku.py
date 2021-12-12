import os
import django_heroku

from root.constants import Environment
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

ALLOWED_HOSTS = ['ntnuisf.herokuapp.com']

# Ensure correct ENV
ENV = Environment.HEROKU

### Environment variables ###
# Values are set in heroku dashboard
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = eval(os.environ['DEBUG'])  # pylint: disable=eval-used

# spotipy
SPOTIFY_SCOPE = os.environ.get('SPOTIFY_SCOPE')
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CACHE_PATH = BASE_DIR / os.environ.get('SPOTIFY_CACHE_PATH')

# django-allauth google provider
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
### End: Environment variables ------------------------------------------------------------

### whitenoise ###
# Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

# whitenoise specifies an exact order, so we do some manipulations.
# https://whitenoise.evans.io/en/stable/django.html#enable-whitenoise
# Set order, extend with previous MIDDLEWARE, finally ensure unique entries
MIDDLEWARE = set([
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
] + MIDDLEWARE)
### End: whitenoise ------------------------------------------------------------

# Activate Django-Heroku.
django_heroku.settings(locals())
