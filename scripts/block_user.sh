#!/bin/bash

source /vagrant/script/dev-env-functions
source ../environment.sh
create_virtual_env "service-frontend"

python manage.py block_user --email=$1
deactivate

echo
echo
echo "Blocked user"
echo
echo
