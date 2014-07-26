import os

class Config(object):
    DEBUG = False
    SEARCH_API = os.environ.get('AUTHENTICATED_SEARCH_API')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_PASSWORD_HASH = 'bcrypt'
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    TEST_USERNAME = os.environ.get('TEST_USERNAME')
    TEST_PASSWORD = os.environ.get('TEST_PASSWORD')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/landregistry_users'

class TestConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    WTF_CSRF_ENABLED = False
    SEARCH_API = 'http://localhost:8003'
    SECRET_KEY = 'verysecret'
    SECURITY_PASSWORD_SALT = SECRET_KEY
