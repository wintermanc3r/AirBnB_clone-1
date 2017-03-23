import unittest
from datetime import datetime
from models import *


class Test_ReviewModel(unittest.TestCase):
    """
    Test the review model class
    """

    def setUp(self):
        self.state = State(**{"name": "Testax"})
        self.city = City(**{"name": "TestCity", "state_id": self.state.id})
        self.user = User(**{"name": "Steve", "email": "example@example.com",
                            "password": "password"})
        self.place = Place(**{"name": "Hotel", "city_id": self.city.id,
                              "user_id": self.user.id})
        self.model = Review(**{"name": "review", "user_id": self.user.id,
                               "place_id": self.place.id, "text": "text"})
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "place_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "text"))
        self.assertEqual(self.model.place_id, self.place.id)
        self.assertEqual(self.model.user_id, self.user.id)
        self.assertEqual(self.model.text, "text")
        self.assertEqual(self.model.name, "review")


if __name__ == "__main__":
    unittest.main()
