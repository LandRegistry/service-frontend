#!/bin/bash

createuser -s landregistry
createdb -U landregistry -O landregistry landregistry_users -T template0

