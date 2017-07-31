""" A controller for authentication tasks, handles login register and logout """
from flask import Blueprint

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth') #pylint: disable=C0103

import app.blueprints.authentication.login #pylint: disable=C0413,W0611
import app.blueprints.authentication.register #pylint: disable=C0413,W0611
import app.blueprints.authentication.logout #pylint: disable=C0413,W0611
