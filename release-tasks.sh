#!/bin/bash
echo "Running Release Tasks"

echo "Running Migrations"
python manage.py makemigrations
python manage.py migrate
echo "Seeding DB"
python manage.py seed --mode=refresh
echo "Done running release-tasks.sh"