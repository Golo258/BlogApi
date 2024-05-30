
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'admin123',
        'HOST': '192.168.56.102',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = [
    '*'
]
DEBUG = False