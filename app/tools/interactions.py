""" A set of tools i made to avoid prebuilt packages like flask-login etc."""
from app.models import User
from app import db, b_crypt


def is_registered(email):
    """
    Returns true if user is registered on the database, searching by email
    @params -> email : string
    @returns -> boolean
    """
    return User.query.filter_by(email=email).first() is not None


def is_authenticated(email, password):
    """
    Returns true if user is authenticated (has correct credentials)
    @params -> email : string , password : string
    @returns -> boolean
    """
    return b_crypt.check_password_hash(User.query.filter_by(email=email).first().password, password)


def add_user_to_database(username, password, email, role, status):
    """
    Void function just for inserting users to the database
    @params -> username, password, email : string
            -> role, status : boolean
    @returns -> absolutely nothing
    """
    try:
        user = User(
            name=username,
            password=b_crypt.generate_password_hash(password),
            email=email,
            role=role,
            status=status
        )
        db.session.add(user)
        db.session.commit()
    except: #pylint: disable=W0702
        db.session.rollback() # Reverts the database
