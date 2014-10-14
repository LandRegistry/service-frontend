#!/bin/bash

source /vagrant/script/dev-env-functions
source ./environment.sh
create_virtual_env "service-frontend"

python manage.py reset_user_view_counts
deactivate

echo
echo
echo "View Count reset for all users"
echo
echo
