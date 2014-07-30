Land Registry Service Front End
===============

[![Build Status](https://travis-ci.org/LandRegistry/service-frontend.svg)](https://travis-ci.org/LandRegistry/service-frontend)

[![Coverage Status](https://img.shields.io/coveralls/LandRegistry/service-frontend.svg)](https://coveralls.io/r/LandRegistry/service-frontend)


### Getting started

```
git clone git@github.com:LandRegistry/service-frontend.git
cd service-frontend
```

#### Run tests

```
pip intall -r test_requirements.txt
```

Then run:

```
py.test
```

### Environment variables needed

```
SETTINGS
AUTHENTICATED_SEARCH_API
SECRET_KEY
```

Local development config:

```
export SETTINGS='config.DevelopmentConfig'
export AUTHENTICATED_SEARCH_API='http://localhost:8003'
export SECRET_KEY='local-dev-not-secret'
```

### Run the app

Run in dev mode to enable app reloading

```
dev/run-app
```

Run tests

```
dev/run-unit-tests
```

### Create a user

Locally:
```
python manage.py create_user --email=auser@gmail.com --password=apassword

```

On Heroku:
```
heroku run python manage.py create_user --email=auser@gmail.com --password=apassword --app lr-service-frontend
```

** This app runs on PORT 8007
