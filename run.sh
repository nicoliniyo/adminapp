#!/bin/bash
source venv/bin/activate
python manage.py runserver
# python -m gunicorn adminapp.asgi:application -k uvicorn.workers.UvicornWorker