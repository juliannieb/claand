"""
Django settings for claand project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tsdx)2ig2869w$)fhgb6ohusy*bqvm-q&63efvkkivu!c(t^=0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# SITE_ID Agregado para que sirva google_calendarize

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'contactos',
    'cotizaciones',
    'empresas',
    'principal',
    'djangobower',
    'django_nvd3',
    'contactos.templatetags.google_calendarize',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'claand.urls'

WSGI_APPLICATION = 'claand.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "prueba1",
        "USER": "prueba",
        "PASSWORD": "hola",
        "HOST": "localhost",
        "PORT": "",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


GRAPPELLI_ADMIN_TITLE = "Claand"


SETTINGS_DIR = os.path.dirname(__file__)


# Path for the template folder
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
)


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/staticfiles/'

LOGIN_URL = '/principal/login/'
LOGOUT_URL = '/principal/logout/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)


STATICFILES_FINDERS = (
    'djangobower.finders.BowerFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components/')

BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
    'd3#3.3.13',
    'nvd3#1.7.1',
)


#BOWER_PATH = '/usr/bin/bower'