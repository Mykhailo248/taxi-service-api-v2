#!/usr/bin/env bash
set -e

echo "Запуск entrypoint.sh …"

# Міграції
python manage.py migrate --noinput

# Старт сервера
python manage.py runserver 0.0.0.0:8000
