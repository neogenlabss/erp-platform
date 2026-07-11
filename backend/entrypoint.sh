#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! python -c "
import psycopg
try:
    psycopg.connect(
        dbname='${DB_NAME}',
        user='${DB_USER}',
        password='${DB_PASSWORD}',
        host='${DB_HOST}',
        port='${DB_PORT}'
    )
    print('Database is ready!')
except Exception:
    raise SystemExit(1)
"
do
    sleep 2
done

echo "Applying migrations..."
python manage.py migrate

echo "Starting Django..."

exec python manage.py runserver 0.0.0.0:8000