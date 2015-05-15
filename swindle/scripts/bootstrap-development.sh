#! /bin/bash

dir='/home/vagrant/swindle/swindle'

# Clear database
python $dir/manage.py flush --noinput

# Create superuser
admin_username="admin"
admin_password="admin"
create_admin="from django.contrib.auth.models import User; User.objects.create_superuser('$admin_username', 'admin@example.com', '$admin_password')"
echo $create_admin | python $dir/manage.py shell