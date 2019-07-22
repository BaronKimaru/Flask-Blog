from flask import Blueprint

#specify name of blueprint 'users' as __name__. specify location of templates
users_blueprint = Blueprint('users', __name__, template_folder='templates', static_folder=None)

from . import routes

