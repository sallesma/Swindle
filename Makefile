################
# django commands

runserver:
	python swindle/manage.py runserver [::]:8000

version:
	python -c "import django; print(django.get_version())"

shell:
	python swindle/manage.py shell