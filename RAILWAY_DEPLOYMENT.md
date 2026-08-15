# Tabbycat on Railway Deployment Guide

## Overview
This guide explains how to deploy Tabbycat to Railway, a modern infrastructure platform.

## Prerequisites
- A Railway account (https://railway.app)
- This repository connected to Railway
- PostgreSQL and Redis databases (Railway will provision these)

## Deployment Steps

### 1. Create a New Railway Project
1. Go to https://railway.app and sign in
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect your GitHub account and select this repository

### 2. Add PostgreSQL Database
1. In your Railway project, click "Add Service"
2. Search for "PostgreSQL" and add it
3. Railway will automatically create a `DATABASE_URL` environment variable

### 3. Add Redis Cache
1. Click "Add Service" again
2. Search for "Redis" and add it
3. Railway will automatically create a `REDIS_URL` environment variable

### 4. Configure Environment Variables
Add these variables to your Tabbycat service in Railway:

```
DJANGO_SETTINGS_MODULE=settings
SECRET_KEY=<generate-a-random-secret-key>
ALLOWED_HOSTS=<your-railway-domain>.up.railway.app,localhost
ON_RAILWAY=true
DEBUG=False
```

To generate a SECRET_KEY:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 5. Deploy
1. Push your code to GitHub
2. Railway will automatically:
   - Build the application (installs dependencies via Pipenv)
   - Collect static files
   - Run database migrations (via the migrate process in Procfile)
   - Start the Gunicorn web server

### 6. Verify
- Access your app at the Railway-provided domain
- Log in with:
  - Username: `admin`
  - Password: `admin` (CHANGE THIS IMMEDIATELY)

## Production Checklist

- [ ] Change the admin password
- [ ] Set `DEBUG=False` in environment variables
- [ ] Generate and set a secure `SECRET_KEY`
- [ ] Configure email settings if needed
- [ ] Set up Sentry for error tracking (optional)
- [ ] Configure allowed domains in `ALLOWED_HOSTS`
- [ ] Back up your database regularly

## Files Modified for Railway

- `railway.json` - Railway build and deploy configuration
- `Procfile` - Process definitions (web server, migrations)
- `tabbycat/settings/railway.py` - Railway-specific Django settings
- `tabbycat/settings/__init__.py` - Updated to detect Railway environment
- `.env.example` - Environment variable template

## Troubleshooting

### Static Files Not Loading
Ensure `python manage.py collectstatic --noinput` runs during build. This is configured in `railway.json`.

### Database Connection Issues
- Verify `DATABASE_URL` environment variable is set
- Check PostgreSQL service is running in Railway
- Ensure migrations run via the Procfile `migrate` process

### Redis Connection Issues
- Verify `REDIS_URL` environment variable is set
- Check Redis service is running in Railway
- Ensure the service can access the Redis port

### Admin Panel Not Accessible
Create a superuser:
```bash
railway run python manage.py createsuperuser
```

## Local Development

To run locally with the same configuration:
```bash
pipenv install --deploy --ignore-pipfile
python manage.py migrate
python manage.py runserver
```

Ensure PostgreSQL and Redis are running locally first.

