#############################
#### third-party imports ####
#############################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#######################
#### local imports ####
#######################
from config import app_config

#########################
#### Initializations ####
#########################
my_orm = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = None #include login.login_view = 'users.login'



def create_app(config_name):
	"""This is the entry into my app"""
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	initialize_extensions(app)
	register_blueprints(app)

	return app


#############################
#### My Helper Functions ####
#############################

def initialize_extensions(app):
	my_orm.init_app(app)
	bcrypt.init_app(app)
	login.init_app(app)

	# Flask-Login configuration
    # from project.models import User

    # @login.user_loader
    # def load_user(user_id):
    #     return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
	from project.posts import posts_blueprint
	from project.home import home_blueprint
	from project.users import users_blueprint

	app.register_blueprint(users_blueprint)
	app.register_blueprint(home_blueprint)
	app.register_blueprint(posts_blueprint)
