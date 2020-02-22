#!/bin/bash
export FLASK_APP=app
export FLASK_ENV=production
export PORT=7331
export SEMI_PROD=True

gunicorn -b 127.0.0.1:$PORT wsgi --timeout 1500 --workers 4 --threads 4