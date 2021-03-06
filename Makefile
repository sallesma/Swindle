################
# django commands

runserver:
	python swindle/manage.py runserver [::]:8000

runcelery:
	cd swindle ; celery -A swindle worker -l info

version:
	python -c "import django; print(django.get_version())"

shell:
	python swindle/manage.py shell

bootstrap-development:
	swindle/scripts/bootstrap-development.sh

test:
	python swindle/manage.py test webapp