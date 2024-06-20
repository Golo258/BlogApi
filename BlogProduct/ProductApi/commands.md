# Packages

django
psycopg2
python-dotenv


# Commands

django-admin startproject project_name

./manage.py runserver

from django.core.management.utils import get_random_secret_key
pytest  -- to run all tests 
pytest -h # print options and config file settings
pip freeze > requirements.txt  # add to requirements list of pip

./manage.py spectacular --file schema.yml

coverage run -m pytest
coverage html
pytest --cov -> give html file content with all test performed on project files 
