"""
Django settings for kc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# -*- coding: UTF-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aain#-_%7dw9e*1*b*+l#9kx7od-iaw(#b*x&wvg($k&iy6%56'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kc.urls'

WSGI_APPLICATION = 'kc.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# External libraries

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'kc', 'media')

STATIC_ROOT = os.path.join(PROJECT_PATH, 'kc', 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'kc', 'site_static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'kc', 'templates'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

FILE_UPLOAD_TEMP_DIR = os.path.join(PROJECT_PATH, 'kc', 'tmp')

EXTERNAL_LIBS_PATH = os.path.join(PROJECT_PATH, 'externals', 'libs')

EXTERNAL_APPS_PATH = os.path.join(PROJECT_PATH, 'externals', 'apps')

sys.path = ['', EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATIC_URL = '/static/'
