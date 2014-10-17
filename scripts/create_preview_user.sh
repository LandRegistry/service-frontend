#!/bin/bash

set -e

if [[ $# -ne 2 ]]; then
    echo "Usage ./create_preview_user.sh someone@email.com password"
    exit 1
fi

export SETTINGS=config.Config

source /vagrant/script/dev-env-functions

source ../environment_preview.sh # i'm assuming you have soemthing like this in lr envs

create_virtual_env "service-frontend"

python manage.py create_user --email=$1 --password=$2 --name='Walter White' --dob='1959-09-07' --gender='M' --current_address='1 High St, London, N1 4LT' --previous_address='2 High St, London, SW2 1LT'

deactivate
