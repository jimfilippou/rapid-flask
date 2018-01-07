""" Sample testing """

from flask_testing import TestCase

from app import app, db, b_crypt
from app.models import User


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User("Rick Grimmes", "rickgrimmes@amc.com", "michowned69")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
