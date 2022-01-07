#!/bin/sh

set -e

nohup gunicorn -k uvicorn.workers.UvicornWorker -c "/opt/gunicorn_conf.py" --pid=/var/run/gunicorn.pid "app.api.public.main:app"