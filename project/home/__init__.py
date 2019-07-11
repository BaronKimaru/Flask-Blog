from flask import Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='project/static')

from . import routes


# http://flask.pocoo.org/docs/1.0/blueprints/#static-files
# static_folder='static'
# url_for('blueprint_name.static', filename='style.css')
