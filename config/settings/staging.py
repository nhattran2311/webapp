from .base import *

DEBUG = True

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