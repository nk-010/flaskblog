from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from dotenv import load_dotenv
import os

# Load variables from .env file
# load_dotenv('/etc/secrets/SECRET_KEY.env')

db= SQLAlchemy()
bcrypt= Bcrypt()
login_manager= LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app():
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URI')
    app.config['SECRET_KEY']= os.environ.get('SECRET_KEY')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app) 

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
