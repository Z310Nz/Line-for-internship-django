#!/usr/bin/env bash
# exit on error
set -o errexit
source venv/bin/activate

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install additional packages like line-bot-sdk and django-allauth
pip install django
pip install line-bot-sdk
pip install django-allauth

# Run Django migrations
python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate
