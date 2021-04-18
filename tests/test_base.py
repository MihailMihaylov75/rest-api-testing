__author__ = "Mihail Mihaylov"
import unittest

from app import app
from db import db


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
        with app.app_context():
            db.init_app(app)
            db.create_all()

        self.app = app.test_client()
        self.app.app_context = app.app_context

    def tearDown(self) -> None:
        with app.app_context():
            db.session.remove()
            db.drop_all()
