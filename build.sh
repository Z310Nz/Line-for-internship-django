#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install line-bot-sdk
pip install django-allauth

python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate