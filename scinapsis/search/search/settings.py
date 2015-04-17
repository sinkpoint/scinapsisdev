"""
Django settings for search project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'guu*(e65ph=nzgc4%g7e@hy5yv%=71h9gl(cfe6^+nlzxwsal3'

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
    'social.apps.django_app.default',
    'search',
    'bootstrapform',
    'debug_toolbar'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
]

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'search.urls'

WSGI_APPLICATION = 'search.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'scp_users',
        'USER': 'root',
        'PASSWORD': 'harahara'
    },
    'search_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'scinapsis',
        'USER': 'root',
        'PASSWORD': 'harahara'
    }
}

DATABASE_ROUTERS = ['search.routers.SearchDbRouter']


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = ''
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
    STATICFILES_DIRS = (
       os.path.join(os.path.dirname(BASE_DIR), "static"),
    )

else:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")


#Template location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(PROJECT_DIR), "templates"),
)


SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY='1379985962300126'
SOCIAL_AUTH_FACEBOOK_SECRET='b99684d153286079f2e15eeb5f6d3506'


