
from .base import *
from django.core.management.utils import get_random_secret_key

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

SECRET_KEY = get_random_secret_key()