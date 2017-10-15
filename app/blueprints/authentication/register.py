""" The Register module, registers the user """
from flask import render_template, redirect, request, session, url_for, flash
from app import db
from app.blueprints.authentication.controller import auth
from app.tools.interactions import is_registered, add_user_to_database

@auth.route('/register', methods=['POST', 'GET'])
def register():
    """
    @get -> Renders register.html
    @post -> Gets email, password, username -> Checks if user is registered
          -> Adds user to database  -> Redirects to index when Registered
    """
    if request.method == 'GET':
        return render_template('auth/register.html')

    username = request.form['usr']
    password = request.form['pwd']
    email = request.form['email']

    if is_registered(email):
        flash("User with that email already exists!")
        return "Error, user with that email already exists!"
    else:
        # Log the user in automatically!
        try:
            add_user_to_database(username, password, email, role=False, status=False)
            session['logged_in'] = True
            session['user'] = username
            return redirect(url_for('index'))
        except: #pylint: disable=W0702
            db.session.rollback()
            return "Whoops"
