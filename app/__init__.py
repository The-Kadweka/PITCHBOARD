from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name):
    
    app = Flask(__name__)
    
    #Creating app configuration
    app.config['SECRET_KEY'] = 'kadweka'

    #Initializing flask extensions
    db.init_app(app)

    return app