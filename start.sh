#!/bin/bash
set -e

# Run migrations
python manage.py migrate --noinput

# Start Gunicorn with the PORT environment variable
PORT=${PORT:-8000}
exec gunicorn tabbycat.wsgi --bind 0.0.0.0:${PORT} --workers 4 --timeout 120

