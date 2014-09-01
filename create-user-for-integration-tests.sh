#!/bin/bash

source /vagrant/script/dev-env-functions
source ./environment.sh
create_virtual_env "service-frontend"
python manage.py create_user --email='citizen@example.org' --password='dummypassword' --name='Walter White' --dob='1959-09-07' --gender='M' --current_address='1 High St, London, N1 4LT' --previous_address='2 High St, London, SW2 1LT'

deactivate
