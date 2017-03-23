import unittest
from datetime import datetime
from models import *


class Test_StateModel(unittest.TestCase):
    """
    Test the state model class
    """

    def setUp(self):
        self.model = State(**{"name": "\"Testax\""})
        self.model.save()

    def tearDown(self):
        self.model.delete()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "Testax")


if __name__ == "__main__":
    unittest.main()
