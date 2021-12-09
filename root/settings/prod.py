import os

from root.constants import Environment
from .base import *  # pylint: disable=wildcard-import, unused-wildcard-import

ALLOWED_HOSTS = []

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = eval(os.environ.get('DEBUG', 'False'))  # pylint: disable=eval-used

# Ensure correct ENV
ENV = Environment.PROD

# Security
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
X_FRAME_OPTIONS = 'SAMEORIGIN'
