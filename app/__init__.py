""" The heart of the flask app """

# Import flask and template operators as long as html Minification and password hashing
from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config.DevelopmentConfig')

# Create the db object
db = SQLAlchemy(app)

# Define password hashing
b_crypt = Bcrypt(app)

# Make sure the user will not mess up
@app.errorhandler(404)
def not_found(err):
    return jsonify(message=str(err)), 404

# Import a module / component using its blueprint handler variable
from app.blueprints.api import api as api_module

# Register blueprint(s)
app.register_blueprint(api_module)


# Just an index rule here, you can add as many as you like.
@app.route('/')
def index():
    return jsonify(
        message="Welcome to the api dear friend"
    )
