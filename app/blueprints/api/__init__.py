from flask import Blueprint, request

api = Blueprint('api', __name__, url_prefix='/v0')

from app.blueprints.api.login import login


@api.route('/', methods=['POST', 'GET'])
def hey():
    """
    Just to make sure every ting works
    """
    if request.method == 'GET':
        return "sup?"




api.add_url_rule('/login', view_func=login, methods=['POST'])

