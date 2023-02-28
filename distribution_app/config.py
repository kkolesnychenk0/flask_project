import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_ECHO = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:qwerty123@localhost/distribution"
    DEBUG = True

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:qwerty123@localhost/test_distribution"

config_dict={
    'dev':DevConfig,
    'test':TestConfig,
}