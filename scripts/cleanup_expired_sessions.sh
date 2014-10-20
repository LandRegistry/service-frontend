#!/bin/bash

source /vagrant/script/dev-env-functions
source ../environment.sh
create_virtual_env "service-frontend"

python manage.py cleanup_expired_sessions

deactivate

echo "Cleared expired sessions"
