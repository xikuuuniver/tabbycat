web: python manage.py migrate --noinput && gunicorn tabbycat.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 4 --timeout 120

