import os
class Config:
    '''
    General configuration parent class
    '''
    pass

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:newa$um0ney@localhost/blog'



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
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:newa$um0ney@localhost/blog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}
