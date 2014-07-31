#!/bin/bash

# TODO: clean up, we're maintaining compatibility with both dev envs

if [[ -f /vagrant/script/checkout ]]; then 
	source /vagrant/script/checkout
else
	source /vagrant/script/dev-env-functions
fi

source ./environment.sh
create_virtual_env "service-frontend"
python manage.py create_user --email=geoff@gmail.com --password=apassword
deactivate
