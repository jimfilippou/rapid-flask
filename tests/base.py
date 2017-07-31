from flask_testing import TestCase

from app import app, db
from app.models import User


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("Bucky", "bucky@thenewboston.com", "12345", True, True))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
