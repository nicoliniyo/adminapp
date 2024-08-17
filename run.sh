#!/bin/bash
source venv/bin/activate
. env_dev.sh
env | grep GROQ
python manage.py runserver
# python -m gunicorn adminapp.asgi:application -k uvicorn.workers.UvicornWorker