import unittest
from datetime import datetime
from models import *


class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def setUp(self):
        self.state = State(**{"name": "Testax"})
        self.city = City(**{"name": "TestCity", "state_id": self.state.id})
        self.user = User(**{"name": "Steve", "email": "example@example.com",
                            "password": "password"})
        self.model = Place(**{"name": "Hotel", "city_id": self.city.id,
                              "user_id": self.user.id})
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenities"))
        self.assertEqual(self.model.city_id, self.city.id)
        self.assertEqual(self.model.user_id, self.user.id)
        self.assertEqual(self.model.name, "Hotel")
        self.assertEqual(self.model.description, "" or None)
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0 or None)
        self.assertEqual(self.model.longitude, 0.0 or None)
        self.assertTrue(self.model.amenities == [''] or
                        self.model.amenities == [])


if __name__ == "__main__":
    unittest.main()
