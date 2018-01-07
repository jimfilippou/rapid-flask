""" The database model schema """
from app import db, b_crypt


class Base(db.Model):

    """ A base class for every other table to inherit """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())


class User(Base):

    """ A user class representing User table """

    __tablename__ = 'auth_user'

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = b_crypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
        return dict(
            name=self.name,
            email=self.password
        )
