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

# music_lbrary

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['ntnuisf.herokuapp.com']

# Values are set in heroku dashboard
SITE_ID = os.environ.get('SITE_ID')

SPOTIFY_SCOPE = os.environ.get('SPOTIFY_SCOPE')
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_CACHE_PATH = os.path.join(BASE_DIR, os.environ.get('SPOTIFY_CACHE_PATH'))

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

#  Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',  # User agent
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

# Activate Django-Heroku.
django_heroku.settings(locals())
