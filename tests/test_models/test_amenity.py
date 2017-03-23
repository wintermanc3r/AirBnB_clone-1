import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """
    Test the amenity model class
    """

    def setUp(self):
        self.model = Amenity(**{"name": "\"steve\""})
        self.model.save()

    def tearDown(self):
        self.model.delete()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "steve")


if __name__ == "__main__":
    unittest.main()
