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


Local development config:

```
export SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql://localhost/service_frontend'
export AUTHENTICATED_SEARCH_API='http://search-api.landregistry.local'
export DECISION_URL='http://decision.landregistry.local'
export MATCHING_URL='http://matching.landregistry.local'
export OWNERSHIP_URL='http://ownership.landregistry.local'
export INTRODUCTION_URL='http://introductions.landregistry.local'
export CASES_URL='http://cases.landregistry.local'
export HISTORIAN_URL='http://historian.landregistry.local'
export OS_API_KEY='no-key'
export REDIS_URL='redis://user:@localhost:6379'
export PERMANENT_SESSION_LIFETIME=60 # minutes picked by random inspiration
export VIEW_COUNT=50
export VIEW_COUNT_ENABLED=True
export SECRET_KEY='localdev-not-secret'
export SECURITY_PASSWORD_HASH='bcrypt'
```

Note in local dev port is assigned by dev env scripts

For production
```
PORT=[SOME NUMBER]
SETTINGS='config.Config'
DATABASE_URL='postgresql://user:password@db_host:port:db_name'
.
.
.
[as above with real values]
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
./create-user-for-integration-tests.sh
```

On Heroku :
```
heroku run python manage.py create_user --email='citizen@example.org' --password='dummypassword' --name='Walter White' --dob='1959-09-07' --gender='M' --current_address='1 High St, London, N1 4LT' --previous_address='2 High St, London, SW2 1LT' --app lr-service-frontend
```

** This app runs on PORT 8007


### Strange things you may find in this application

User accounts and login

This application has a notion of users in a form that would not need to exist if/when integration with GOV.UK Verify happens.

In this application a user logs in with a user name and password. That is used to lookup in the applications local database a set of personal data (name, date of birth, gender, current address and previous address). This personal data set is used to lookup a "matching" record in the matching service.

If we were to use GOV.UK Verify the login form and user name + password check happens in an external service (GOV.UK Verify) which then returns the personal data set to use for matching. Make sense?

We took a shortcut here by being handwavy about where the personal data comes from. Since we did not do GOV.UK Verify integration and we did not want to build a stub GOV.UK Verify in the alpha, it really did not matter that we just held our fake set of personal data in the application db proper.

When GOV.UK Verify integration comes about the user object as is would mutate into some sort of login record table. The login view method would still make a call out to matching but the input to that call would be something that came from GOV.UK Verify.


##### Create Debian package

```
cd packaging
./build.sh
```

This will create a virtualenv, install service-frontend into that env. Then it will set virtualenv paths to match the eventual installation directory of the debian package that is the output of build.sh.

**Note**
The packaging of a virtualenv using fpm may soon be much easier depending on [outcome of this](https://github.com/jordansissel/fpm/issues/697)

The result of running ./build.sh is debian package will be created in packaging called service-frontend. The package has a basic upstart config, empty pre and post install and remove scripts. For the moment the installer is set to install to /opt/alpha/service-frontend. Change as required. Also post install does not set ownership or permissions on the installed package.

**Before installing in a production box you should:**

* Set the environment variables as listed in environnment.sh **(put the file into the package install dir - have config management tool do this)**
* Create a no login user account that the service-frontend service can be owned by and run as (at the moment in a dev vagrant it runs as root)

##### To install the debian package

```
sudo dpkg -i service-frontend_0.1_all.deb
```

Then run

```
sudo start service-frontend
```

Note that this assumes you have set all the correct environment variables.

To uninstall

```
sudo dpkg -r service-frontend
```

##### Database migrations

At the moment the migration version files and manage.py are included in packages and live in installation directory. I would for the moment run these after the install (and under control of configuration management tool) before running the service.

```
cd /opt/alpha/service-frontend
python manage.py db upgrade
```



