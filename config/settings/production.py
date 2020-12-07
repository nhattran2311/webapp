from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # 'NAME': 'fantastic_db',
#         # 'USER': 'postgres',
#         # 'PASSWORD': 'Winter19!',
#         'CONN_MAX_AGE': 500
#         # 'HOST':'localhost',
#         # 'PORT':'5432',
#     }
# }
import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)