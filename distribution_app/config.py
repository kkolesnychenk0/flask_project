import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_ECHO = True
    DEBUG = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:qwerty123@localhost/distribution"

config_dict={
    'dev':DevConfig,
}