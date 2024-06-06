#!/bin/bash
source venv/bin/activate
python manage.py collectstatic

# Copiamos el directorio para i18n
cp -r locale staticfiles/

python manage.py runserver
# python -m gunicorn adminapp.asgi:application -k uvicorn.workers.UvicornWorker