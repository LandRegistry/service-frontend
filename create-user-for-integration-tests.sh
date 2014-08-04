#!/bin/bash

source /vagrant/script/dev-env-functions
source ./environment.sh
create_virtual_env "service-frontend"
python manage.py create_user --email=citizen@example.org --password=dummypassword

deactivate
