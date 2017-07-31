""" The login module, logs the user in """
from flask import request, session, redirect, url_for, render_template, flash
from app.models import User
from app.blueprints.tools.db import is_authenticated, is_registered
from app.blueprints.authentication.controller import auth

@auth.route('/login', methods=['POST', 'GET'])
def login():
    """
    @get -> Renders the login.html
    @post -> Gets email and password -> Checks if user is registered
          -> Checks if user is authenticated -> Redirects to index when logged in
    """
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form['eml']
    password = request.form['pwd']
    if is_registered(email):
        if is_authenticated(email, password):
            # Log the user in
            session['logged_in'] = True
            session['user'] = User.query.filter_by(email=email).first().name
            return redirect(url_for('index'))

        flash("Wrong Credentials")
        return render_template('auth/login.html')

    flash("You are not registered!")
    return render_template('auth/login.html')
