import os
class Config:
    '''
    General configuration parent class
    '''
    
#email configurations
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
class TestConfig(Config):
    '''
    Test configuration child class
    Args:
    Config: The parent configuration class with general configuration settings
    '''
    DATABASE_PASS = os.environ.get('DATABASE_BASE')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadweka@localhost/blog_test'

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
