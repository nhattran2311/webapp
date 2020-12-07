from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fantastic_db',
        'USER': 'postgres',
        'PASSWORD': 'Winter19!',
        # 'HOST':'localhost',
        # 'PORT':'5432',
    }
}