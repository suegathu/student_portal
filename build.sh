#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Ensure staticfiles directory exists
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --noinput --clear -v 0

# Run migrations
python manage.py migrate --noinput

# Test basic server (non-blocking)
python manage.py check --deploy || echo "Warning: Deployment checks failed"

# Make sure permissions are correct
chmod +x ./manage.py