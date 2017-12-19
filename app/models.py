""" The database model schema """
from app import db


class Base(db.Model):

    """ A base class for every other table to inherit """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base):

    """ A user class representing User table """

    __tablename__ = 'auth_user'

    # User Name
    name = db.Column(db.String(128), nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # Authorisation Data: role & status
    role = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password, role, status):

        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
        return dict(
            name     = self.name,
            email    = self.password,
            password = self.password,
            rol      = self.role,
            status   = self.status
        )
