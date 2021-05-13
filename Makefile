start:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

install:
	pip install -r requirements.txt


