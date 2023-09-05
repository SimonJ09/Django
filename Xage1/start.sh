#!/bin/bash
python manage.py makemigrations
python manage.py migrate

gunicorn xage1.wsgi:application --bind 0.0.0.0:$PORT --workers 4
