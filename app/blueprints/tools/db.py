from app.blueprints.authentication.models import User
from app import db, b_crypt


def is_registered(email):
    return User.query.filter_by(email=email).first() is not None


def is_authenticated(email, password):
    return b_crypt.check_password_hash(User.query.filter_by(email=email).first().password, password)


def add_user_to_database(username, password, email, role, status):
    try:
        user = User(
            name=username,
            password=b_crypt.generate_password_hash(password),
            email=email,
            role=role,
            status=False
        )
        db.session.add(user)
        db.session.commit()
    except Exception as manager_rugby:
        print manager_rugby.message
        db.session.rollback()
