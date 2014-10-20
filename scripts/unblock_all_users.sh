#!/bin/bash

source /vagrant/script/dev-env-functions
source ../environment.sh
create_virtual_env "service-frontend"

python manage.py unblock_all_users

deactivate

echo "Unblocked all users"
