#!flask/bin/python3
import os
import unittest

from config import basedir
from app import app, db

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app-test.db')

        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_generic(self):
        assert 1 + 1 == 2

if __name__ == '__main__':
    unittest.main()
