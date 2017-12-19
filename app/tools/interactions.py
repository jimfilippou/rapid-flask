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


def add_user_to_database(username, password, email):
    """
    Void function just for inserting users to the database
    @params -> username, password, email : string
    @returns -> the user object, you can use it or not, i don't care
    """
    try:
        user = User(
            name=username,
            password=b_crypt.generate_password_hash(password),
            email=email
        )
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
