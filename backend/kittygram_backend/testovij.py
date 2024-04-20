from dotenv import load_dotenv

import os

from django.core.management.utils import get_random_secret_key


load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY', default=get_random_secret_key())

DEBUG = str(os.getenv('DEBUG', default='')).lower() == 'true'

ALLOWED_HOSTS = str(os.getenv('ALLOWED_HOSTS', default='localhost 127.0.0.1')).split()

print(SECRET_KEY)
print(DEBUG)
print(ALLOWED_HOSTS)