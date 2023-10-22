runserver:
	python manage.py runserver 8007

migrate:
	python manage.py makemigrations
	python manage.py migrate

get-secret-key:
	python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
