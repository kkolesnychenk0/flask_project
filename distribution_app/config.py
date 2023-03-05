"""Configuration module"""
import os

class Config():
    """general settings """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_ECHO = True

class DevConfig(Config):
    """development settings"""
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:qwerty123@localhost/distribution"
    DEBUG = True

class TestConfig(Config):
    """testing settings"""
    TESTING=True
    #SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root:qwerty123@localhost/test_distribution"
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

config_dict={
    'dev':DevConfig,
    'test':TestConfig,
}
