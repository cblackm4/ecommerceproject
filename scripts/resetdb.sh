#!/bin/bash

cd ./api

#remove migrations files and db
rm -rf ./administration/migrations ./pawkages/migrations
rm -f db.sqlite3

# setup db
python manage.py makemigrations administration pawkages
python manage.py migrate

# create super user account
echo "from administration.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

cd ..