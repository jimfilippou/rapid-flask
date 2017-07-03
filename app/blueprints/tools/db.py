from app.blueprints.authentication.models import User
from app import db, b_crypt

# Returns true if user is registered on the database
# Argument/s -> email : string
def is_registered(email):
    return User.query.filter_by(email=email).first() is not None

# Returns true if user is authenticated on login
# Argument/s -> email : string , password : string
def is_authenticated(email, password):
    return b_crypt.check_password_hash(User.query.filter_by(email=email).first().password, password)

# Void function just for inserting users to the database
# Argument/s -> username : string , password : string , role : boolean , status : boolean
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
