import os

class Config(object):
    DEBUG = False
    AUTHENTICATED_SEARCH_API = os.environ['AUTHENTICATED_SEARCH_API']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DECISION_URL = os.environ['DECISION_URL']
    SECRET_KEY = os.environ['SECRET_KEY']
    WTF_CSRF_ENABLED = True
    MATCHING_URL = os.environ['MATCHING_URL']
    OWNERSHIP_URL = os.environ['OWNERSHIP_URL']
    OS_API_KEY = os.environ['OS_API_KEY']
    INTRODUCTION_URL = os.environ['INTRODUCTION_URL']


    # optional and only needed on heroku so get
    # safely
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DECISION_URL = 'http://decision.landregistry.local'

class TestConfig(DevelopmentConfig):
    TESTING = True
