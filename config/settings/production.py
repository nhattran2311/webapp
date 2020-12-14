from .base import *

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com']


import dj_database_url
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)