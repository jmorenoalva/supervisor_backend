run:
	python manage.py runserver

collect:
	python manage.py collectstatic

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

migra: makemigrations migrate