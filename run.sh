#!/bin/bash

export SETTINGS='config.DevelopmentConfig'
export AUTHENTICATED_SEARCH_API='http://localhost:8003'
export SECRET_KEY='''T\xdf\xa2\x0f\x10&\x10\xad9\xa5\xd0\xa6f\x88\x95`\xb0"\x10F\x19L\x89S'''

createuser -s landregistry
createdb -U landregistry_users -O landregistry landregistry -T template0

python manage.py db upgrade
python run_dev.py

python run_dev.py
