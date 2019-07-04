#third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import app_config

#initialize sqlalchemy class
my_orm = SQLAlchemy()

def create_app(config_name):
	"""This is the entry into my app"""
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	my_orm.init_app(app)

	@app.route('/')
	def index():
		"""testing index"""
		return "Index Page"


	return app



