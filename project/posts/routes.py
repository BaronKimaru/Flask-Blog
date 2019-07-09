#############################
#### third-party imports ####
#############################

from flask import render_template

#########################
##### local imports #####
#########################
from . import posts_blueprint
from project.articles import articles

Posts = articles()

@posts_blueprint.route('/posts')
def posts():
    """Display All Posts"""
    return render_template('posts.html', posts = Posts)

@posts_blueprint.route('/post/<string:id>')
def post(id):
    """Display A Specific Post"""
    return render_template('post.html', id = id)