#!/bin/sh

# Чекати готовність PostgreSQL
echo "Waiting for db..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.5
done

# Чекати готовність Redis
echo "Waiting for redis..."
REDIS_HOST=$(echo $REDIS_URL | awk -F[/:] '{print $4}')
REDIS_PORT=$(echo $REDIS_URL | awk -F[/:] '{print $5}')
while ! nc -z $REDIS_HOST $REDIS_PORT; do
  sleep 0.5
done

# Міграції Django
python manage.py migrate

# Запуск команди, переданої з docker-compose
exec "$@"
