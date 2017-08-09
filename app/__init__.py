""" The heart of the flask app """

# Import flask and template operators as long as html Minification and password hashing
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from htmlmin import minify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the application object
app = Flask(__name__) #pylint: disable=C0103

# Configurations
app.config.from_object('config.DevelopmentConfig')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app) #pylint: disable=C0103

# Define password hashing
b_crypt = Bcrypt(app) #pylint: disable=C0103

# Make sure the user wont mess up
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.blueprints.authentication.controller import auth as authentication_module  #pylint: disable=C0413

# Register blueprint(s)
app.register_blueprint(authentication_module)

@app.after_request
def response_minify(response):
    """ Minify reponses for a slightly faster reponse after request"""
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
        )
        return response
    return response


# Just an index rule here, you can add as many as you like.
@app.route('/')
def index():
    return render_template('welcome.html')
