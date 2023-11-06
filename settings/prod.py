import os
from .base import *
import pymysql
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']  #PARA QUE CUALQUIERA IP SE CONECTE

# DEBUG = False
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

pymysql.version_info = (1, 4, 6, 'final', 0)

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('NAME_DATABASE'),
        'USER': os.getenv('USER_DATABASE'),
        'PASSWORD': os.getenv('PASSWORD_DATABASE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')