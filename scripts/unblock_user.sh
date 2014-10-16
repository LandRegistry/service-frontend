#!/bin/bash
source /vagrant/script/dev-env-functions
source ../environment.sh
create_virtual_env "service-frontend"

python manage.py unblock_user --email=$1
deactivate

echo
echo
echo "User unblocked"
echo
echo
