#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# Run migrations
python manage.py migrate --noinput

# Test basic server (non-blocking)
python manage.py check --deploy || echo "Warning: Deployment checks failed"

# Make sure permissions are correct
chmod +x ./manage.py