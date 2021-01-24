import json
import os
from pathlib import Path

import environ
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

# setup django-environ
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'env/.env'))

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # django allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # django extensions
    'django_extensions',
    # django debug toolbar
    'debug_toolbar',
    # simple captcha
    'captcha',

    # my apps
    'apps.core.apps.CoreConfig',
    'apps.snippet.apps.SnippetConfig',
    'apps.authentication.apps.AuthenticationConfig',
    'apps.profiles.apps.ProfilesConfig',
]

SITE_ID = 1

# setup django-allauth google provider
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '583031924238-2sntg2osu8b3q17u0kc3qf0pd0t7oop7.apps.googleusercontent.com',
            'secret': '5MoGSEpDZSO-2eo1A3MGDXzC',
            'key': ''
        }
    }
}

AUTHENTICATION_BACKENDS = [
    # required by django-allauth
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # middleware for url i18n
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django debug toolbar middleware
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# for django debug toolbar
INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'coderators.root_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coderators.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        "HOST": env('HOST'),
        "PORT": env('PORT'),
        "USER": env('USER'),
        "PASSWORD": env('PASSWORD')
    }
}

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

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_USE_SSL = env('EMAIL_USE_SSL', default=False)
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default=False)
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# Internationalization and localization
# Default language
LANGUAGE_CODE = 'en'

# Limit available languages to:
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
]

# Translation files (.po and .mo files) location
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Override the default 'django-language' cookie name
LANGUAGE_COOKIE_NAME = 'user-language'

# Enable i18n and l10n
USE_I18N = True
USE_L10N = True
USE_THOUSAND_SEPARATOR = True

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps/core/static'),
    os.path.join(BASE_DIR, 'apps/snippet/static'),
]

# image files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Login defaults
LOGIN_URL = reverse_lazy('authentication:login')
LOGIN_REDIRECT_URL = reverse_lazy('snippet:home')

# Setup custom user model
AUTH_USER_MODEL = 'authentication.CustomUser'

# Setup django-allauth with custom user
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
