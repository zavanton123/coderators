import json
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

# Choose debug or prod secrets
if DEBUG:
    secrets_filename = 'secrets-debug.json'
else:
    secrets_filename = 'secrets-prod.json'

# get private data from json file (untracked by git)
with open(os.path.join(BASE_DIR, secrets_filename)) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, source=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return source[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


SECRET_KEY = get_secret('SECRET_KEY')

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snippet.apps.SnippetConfig',
    # simple captcha
    'captcha',
    # django debug toolbar
    'debug_toolbar'
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

ROOT_URLCONF = 'coderators.urls'

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
        'ENGINE': get_secret('ENGINE'),
        'NAME': get_secret('NAME'),
        "HOST": get_secret('HOST'),
        "PORT": get_secret('PORT'),
        "USER": get_secret('USER'),
        "PASSWORD": get_secret('PASSWORD')
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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = get_secret('DEFAULT_FROM_EMAIL')

# Internationalization and localization
# Default language
LANGUAGE_CODE = 'en'

# Limit available languages to:
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('de', _('German')),
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

TIME_ZONE = 'Europe/Moscow'
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'snippet/static')
]

# Default login url
LOGIN_URL = "/auth/login"
