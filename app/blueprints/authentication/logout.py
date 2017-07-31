""" The logout module, logs the user out """
from functools import wraps
from flask import session, redirect, url_for, flash
from app.blueprints.authentication.controller import auth

def login_required(f): #pylint: disable=C0103
    """ Decorator triggered to identify if logged in """
    @wraps(f)
    def wrap(*args, **kwargs):
        """ Wraps args and returns them if the user is logged in """
        if 'logged_in' in session:
            return f(*args, **kwargs)

        flash("You need to login.")
        return redirect(url_for('auth'))

    return wrap

@auth.route('/logout')
@login_required
def logout():
    """
    @get -> Logs the user out -> redirect to index
    """
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect(url_for('index'))
