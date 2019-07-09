#############################
#### third-party imports ####
#############################

from flask import render_template

#########################
##### local imports #####
#########################
from . import home_blueprint

@home_blueprint.route('/')
def index():
    """main Home Page"""
    return render_template('home/index.html')


@home_blueprint.route('/about')
def about():
    """About Page"""
    return render_template("home/about.html")

@home_blueprint.route('/contact')
def contact():
    """Contact Page"""
    return render_template("home/contact.html")