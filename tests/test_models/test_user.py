import unittest
from datetime import datetime
from models import *


class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        self.model = User(**{"name": "Steve",
                             "email": "example@example.com",
                             "password": "hello",
                             "first_name": "steve",
                             "last_name": "bob"})
        self.model.save()

    def tearDown(self):
        self.model.delete()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "example@example.com")
        self.assertEqual(self.model.password, "hello")
        self.assertEqual(self.model.first_name, "steve")
        self.assertEqual(self.model.last_name, "bob")


if __name__ == "__main__":
    unittest.main()
