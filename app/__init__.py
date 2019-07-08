#third-party imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#local imports
from config import app_config
from app.articles import posts

#initialize sqlalchemy class
my_orm = SQLAlchemy()
Posts = posts()
print("posts: ", Posts)

def create_app(config_name):
	"""This is the entry into my app"""
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	my_orm.init_app(app)

	@app.route('/')
	def index():
		"""testing index"""
		return render_template("home.html")

	@app.route('/about')
	def about():
		"""About Page"""
		return render_template("about.html")

	@app.route('/posts')
	def posts():
		"""Display All Posts"""
		return render_template('posts.html', posts = Posts)

	@app.route('/post/<string:id>')
	def post(id):
		"""Display A Specific Post"""
		return render_template('post.html', id = id)


	return app



