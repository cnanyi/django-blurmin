"""
Django settings for djangui project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'en=4x7givvfk3j8x(4uxrb+qywm)z!qt96l(-@9x8p3f8hwn2k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # 'channels',
    # 'webcoders',
    'ui',
    'ui.notifications',
    'ui.dashboard',
    'myapp'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ui.middleware.UIMiddleWare',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#------------------------- ui changes !! start

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip("/"))

ADMIN_LOCATION = 'dashboard/'

LOGIN_URL = '/' + ADMIN_LOCATION + 'ui/loginview/'
LOGIN_REDIRECT_URL = '/' + ADMIN_LOCATION
BLURMIN_DEVMODE = True

ADMIN_MENU = 'myapp.blurmin_menu.menu'

DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i'


DATE_INPUT_FORMATS = [
    '%Y-%m-%d',
]

MEDIA_URL = STATIC_URL + "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, *MEDIA_URL.strip("/").split("/"))

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "ui.routing.channel_routing",
    },
}

# SESSION_ENGINE = 'ui.session'
# SESSION_FILE_PATH = BASE_DIR + '/../SESSION'
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
# SESSION_COOKIE_NAME = 'myproject'
# # enabled for reading cookie from javascript!!!
# SESSION_COOKIE_HTTPONLY=False
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_COOKIE_AGE = 12 * 60 * 60

# FILEBROWSER_FILTER = 'ma.filebrowser.filter'

# FILE_BROWSER = {'DIRECTORY': 'uploads/company/',}


# MOVER_ADMIN_URL='/dashboard/'
# AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)
# MOVER_ADMIN_FULL_URL = 'https://www.movingauthority.com/dashboard'

# from dependent_settings import *


LOGENTRY_MODEL_CLASS = 'django.contrib.admin.models.LogEntry'
# CHANGELOG_MODEL_CLASS = 'webcoders.models.ChangeLog'
# TINYMCE_SETUP_JS = ''
# from local_settings import *