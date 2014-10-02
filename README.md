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

#### Create/Update database

There's an intial migration script in the project created using Flask-Migrate so you just need to call the following

```
python manage.py db upgrade
```

If you need to run this on Heroku, use this command:
```
heroku run python manage.py db upgrade --app lr-service-frontend
```
Note that this is run automatically as part of the deploy from travis

Run the upgrade command whenever you have additional migrations

### Run the app

Run in dev mode to enable app reloading

```
dev/run-app
```

Run tests

```
dev/run-unit-tests
```

### To create a user

First activate the virualenv for this project

Locally:
```
python manage.py create_user --email=auser@gmail.com --password=apassword

```

On Heroku :
```
heroku run python manage.py create_user --email=auser@gmail.com --password=apassword --app lr-service-frontend
```

** This app runs on PORT 8007
