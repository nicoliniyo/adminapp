#!/bin/bash
source venv/bin/activate
. env_dev.sh
env | grep GROQ
python manage.py collectstatic

# Copiamos el directorio para i18n
cp -r locale staticfiles/

python manage.py runserver
# python -m gunicorn adminapp.asgi:application -k uvicorn.workers.UvicornWorker