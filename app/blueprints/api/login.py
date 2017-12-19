""" API LOGIN functionality """
from datetime import datetime, timedelta
from flask import request, jsonify
from jwt import encode
from app import app, b_crypt
from app.models import User
from app.blueprints.api import api


def login():
    """ Log the damn user in """

    auth = request.authorization

    if app.config["DEBUG"]:
        if auth:
            print "Received auth -> %s %s" % (auth.username, auth.password)
        else:
            print "Could not receive auth\n\n%s\n\n%s" % (request.headers, request.data)

    if not auth or not auth.username or not auth.password or request.headers['Content-Type'] != 'application/json':
        return jsonify(token=None), 400

    user = User.query.filter_by(email=auth.username).first()

    if not user:
        return jsonify(token=None), 404

    if b_crypt.check_password_hash(user.password, auth.password):

        # Generate a token
        token = encode(
            dict(
                id=user.id,
                exp=datetime.utcnow() + timedelta(minutes=15)
            ),
            app.config['SECRET_KEY']
        )

        # Send back the token
        return jsonify(token=token.decode('UTF-8')), 200

    # Not authorized
    return jsonify(token=None), 401
