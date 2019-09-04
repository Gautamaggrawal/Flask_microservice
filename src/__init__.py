from flask import Flask
from .auth import auth as auth_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from .models import db,User


def create_app():
    flask_app = Flask(__name__,template_folder='templates')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    flask_app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)

    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    print(db,"sadfgbfsaSDF")


    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))


    flask_app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    # from .app import main as main_blueprint
    # flask_app.register_blueprint(main_blueprint)

    return flask_app
