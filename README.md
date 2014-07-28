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
export SETTINGS='conig.Config'
```


### Run the app

Run in dev mode to enable app reloading

```
./run.sh dev
```

Otherwise with foreman

```
./run.sh
```

** This app runs on PORT 8007
