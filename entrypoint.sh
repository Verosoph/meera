#!/bin/sh
python ./meera/manage.py makemigrations
python ./meera/manage.py migrate
exec "$@"