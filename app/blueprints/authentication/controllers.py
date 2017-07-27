# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, session, redirect, url_for

# Import the database object from the main app module
from app import db

# Import module models (i.e. User)
from app.models import User

# Import tools
from app.blueprints.tools.db import is_authenticated, is_registered, add_user_to_database

# Import requests library for api calls
from requests import post

# Import yml loader
from yaml import safe_load

# Import wraps
from functools import wraps

# Load api keys
with open("app/blueprints/authentication/apis.yml", 'r') as stream:
    data = safe_load(stream)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
auth = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login.")
            return redirect(url_for('auth'))

    return wrap


@auth.route('/', methods=['GET'])
def authentication():
    if 'logged_in' in session:
        if session['logged_in'] is True:
            return "already logged in bro"
    else:
        return render_template("auth/auth.html")


@auth.route('/login', methods=['POST'])
def login():
    email = request.form['eml']
    password = request.form['pwd']
    if is_registered(email):
        if is_authenticated(email, password):
            # Log the user in
            session['logged_in'] = True
            session['user'] = User.query.filter_by(email=email).first().name
            return redirect(url_for('index'))
        else:
            flash("Wrong Credentials")
            return render_template('auth/auth.html')
    else:
        flash("You are not registered!")
        return render_template('auth/auth.html')


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            # recaptcha thing here
            response = post("https://www.google.com/recaptcha/api/siteverify",
                            data={
                                "secret": data['recaptc'],
                                "response": request.form['g-recaptcha-response']
                            })

        except:
            response = None

        if response and response.json()['success']:

            # Get user stuff when recaptca success

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
                except:
                    db.session.rollback()
                    return "Whoops"
        else:
            flash("You didn't pass human verification test.")
            return "You didn't pass human verification test."


@auth.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('index'))
