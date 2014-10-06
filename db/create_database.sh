#!/bin/bash

createuser -s service_frontend
createdb -U service_frontend -O service_frontend service_frontend -T template0

