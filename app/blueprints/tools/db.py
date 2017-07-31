""" A set of tools i made to avoid prebuilt packages """
from app.models import User
from app import db, b_crypt


def is_registered(email):
    """ Returns true if user is registered on the database """
    return User.query.filter_by(email=email).first() is not None


def is_authenticated(email, password):
    """ Returns true if user is authenticated on login """
    return b_crypt.check_password_hash(User.query.filter_by(email=email).first().password, password)


def add_user_to_database(username, password, email, role, status):
    """
    Void function just for inserting users to the database
    @params -> username, password, email -> string
            -> role, status -> bool
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
        db.session.rollback()
