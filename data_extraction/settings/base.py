"""
Django settings for data_extraction project.
Generated by 'django-admin startproject' using Django 3.2.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
    'storages',
    'django.contrib.sites',
    #'background_task',
    'data_extraction',
    'administration',
    'search',
    'api',
    'file_manager',
    'interpretation',
]
SITE_ID=1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'data_extraction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'data_extraction.wsgi.application'



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

TIME_ZONE = 'Australia/Brisbane'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/home/'

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "interpretation/data-extraction-276505-c6b99822c08c.json"

# LOGGING
# DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {name}:{message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {name}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": env('LOG_PATH') + "/fluid_data.log",
            "formatter": "verbose",
        },
    },
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
       # '': {
       #     'handlers': ['console','file'], 
       #     'level': 'WARNING',
       #     'propagate': True,
       # },
        'data_extraction': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_DATA_EXTRACTION'),
            'propagate': True,
        },
        'celery_tasks': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_CELERY_TASKS'),
            'propagate': True,
        },
        'file_manager': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_FILE_MANAGER'),
            'propagate': True,
        },
        'search': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_SEARCH'),
            'propagate': True,
        },
        'interpretation': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_INTERPRETATION'),
            'propagate': True,
        },
        'administration': {
            'handlers': ['console','file'], 
            'level': env('LOG_LEVEL_ADMIN'),
            'propagate': True,
        },
    },
}



AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
#EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# REDIS related settings 
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout':3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_WORKER_CONCURRENCY = 1
CELERY_WORKER_PREFETCH_MULTIPLIER = 1


