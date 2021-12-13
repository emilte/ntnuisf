"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

STATIC_URL = '/static/'
STATIC_ROOT = 'staticroot'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'mediaroot'

# URLs
LOGIN_REDIRECT_URL = 'accounts:profile'
LOGIN_URL = 'accounts:login'
LOGOUT_REDIRECT_URL = 'accounts:login'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'root',  # register to enable management.commands
    'ntnuisf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
            },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

### compressor / django-libsass ###
INSTALLED_APPS += [
    'compressor',
]

COMPRESS_PRECOMPILERS = (('text/x-scss', 'django_libsass.SassCompiler'), )

STATICFILES_FINDERS += [
    'compressor.finders.CompressorFinder',
]
# End: compressor / django-libsass --------------------------------------------------------------

### django-debug-toolbar ###
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_COLLAPSED': True,
}
### End: django-debug-toolbar --------------------------------------------------------------

### django-allauth ###

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

INSTALLED_APPS += [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = int(os.environ['SITE_ID'])
### End: django-allauth --------------------------------------------------------------

### user-agents ###

# INSTALLED_APPS += [
#     'django_user_agents',  # Recognises devices and touch capabilities
# ]

# # Cache backend is optional, but recommended to speed up user agent parsing
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# MIDDLEWARE += [
#     'django_user_agents.middleware.UserAgentMiddleware',
# ]

# # Name of cache backend to cache user agents. If it not specified default
# # cache alias will be used. Set to `None` to disable caching.
# USER_AGENTS_CACHE = 'default'
### End: user-agents --------------------------------------------------------------

### django-extensions ###

### End: django-extensions --------------------------------------------------------------

### TinyMCE ###
# INSTALLED_APPS += [
#     'tinymce',  # For HTMLField (obsolete, tinyMCE is used another way)
# ]
# also in urlpatterns
### End: TinyMCE --------------------------------------------------------------

### django-select2 ###
# INSTALLED_APPS += [
#     'django_select2',  # For improved ChoiceField widgets
# ]
### End: django-select2 --------------------------------------------------------------

### django-seed ###
# INSTALLED_APPS += [
#     'django_seed',  # Seed database easily
# ]
### End: django-seed --------------------------------------------------------------

### ??? ###
# INSTALLED_APPS += [
#     '???',
# ]
### End: ??? --------------------------------------------------------------

### django-extensions ###
INSTALLED_APPS += [
    'django_extensions',  # Extended CLI commands
]
### End: django-extensions --------------------------------------------------------------

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
