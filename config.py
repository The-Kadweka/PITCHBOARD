import os

class Config:
    """
    This is the parent class which will have the general configurations
    """
    UPLOADED_PHOTOS_DEST = "app/static/photos"
    SECRET_KEY = os.environ.get("kadweka")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kadweka@tony/blog'

class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
