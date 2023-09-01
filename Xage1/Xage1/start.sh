#!/bin/bash

pip install --upgrade typing-extensions

# Lancement de Gunicorn avec votre application Django
gunicorn xage.wsgi:application --bind 0.0.0.0:$PORT --workers 4