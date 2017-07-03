# Import flask and template operators as long as html Minification and password hashing
from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from htmlmin import minify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Define password hashing
b_crypt = Bcrypt(app)

# Make sure the user wont messes up
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.blueprints.authentication.controllers import auth as authentication_module

# Register blueprint(s)
app.register_blueprint(authentication_module)

# Minify reponses for a slightly faster reponse
@app.after_request
def response_minify(response):
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
        )
        return response
    return response


# Just an index rule here
@app.route('/')
def index():
    return render_template('welcome.html')
