#!/bin/bash

echo "Creating database for service-frontend"

createuser -s landregistry
createdb -U landregistry -O landregistry landregistry_users -T template0

