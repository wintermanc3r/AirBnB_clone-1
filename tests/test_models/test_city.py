import unittest
from datetime import datetime
from models import *


class Test_CityModel(unittest.TestCase):
    """
    Test the city model class
    """

    def setUp(self):
        self.state = State(**{"name": "Testax"})
        self.model = City(**{"name": "city", "state_id": self.state.id})
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "city")
        self.assertEqual(self.model.state_id, self.state.id)


if __name__ == "__main__":
    unittest.main()
