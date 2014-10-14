import os
from datetime import timedelta

class Config(object):
    DEBUG = False
    AUTHENTICATED_SEARCH_API = os.environ['AUTHENTICATED_SEARCH_API']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    CASES_URL = os.environ['CASES_URL']
    SECRET_KEY = os.environ['SECRET_KEY']
    MATCHING_URL = os.environ['MATCHING_URL']
    OWNERSHIP_URL = os.environ['OWNERSHIP_URL']
    OS_API_KEY = os.environ['OS_API_KEY']
    INTRODUCTION_URL = os.environ['INTRODUCTION_URL']
    HISTORIAN_URL = os.environ['HISTORIAN_URL']
    REDIS_URL = os.environ['REDIS_URL']
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=int(os.environ['PERMANENT_SESSION_LIFETIME']))
    WTF_CSRF_ENABLED = True
    VIEW_COUNT = int(os.environ['VIEW_COUNT'])
    VIEW_COUNT_ENABLED = os.environ['VIEW_COUNT_ENABLED']


    # optional and only needed on heroku so get
    # safely
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False

class TestConfig(DevelopmentConfig):
    TESTING = True
    VIEW_COUNT_ENABLED = False
