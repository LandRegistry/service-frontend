#!/bin/bash

source /vagrant/script/dev-env-functions
source ./environment.sh
create_virtual_env "service-frontend"

python manage.py reset_single_user_view_count --email=$1
deactivate

echo
echo
echo "View Count reset for users"
echo
echo
