#!/usr/bin/python3
"""
test for place class
"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """
    Test Place
    """

    def setUp(self):
        """
        Defines place object
        """
        self.test_place = Place()

    def test_inherits_basemodel(self):
        """ check for inheritance
        """
        self.assertIsInstance(self.test_place, BaseModel)

    def test_cityid(self):
        """ Tests that the city_id"""
        self.assertTrue(hasattr(Place, 'city_id'))

    def test_cityid_type(self):
        """ Test city id type"""
        self.assertIsInstance(Place.city_id, str)

    def test_userid(self):
        """ Test if  user_id exists"""
        self.assertTrue(hasattr(Place, 'user_id'))

    def test_userid_type(self):
        """ Test the user_id type"""
        self.assertIsInstance(Place.user_id, str)

    def test_name(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'name'))

    def test_name_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.name, str)

    def test_description(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'description'))

    def test_description_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.description, str)

    def test_number_rooms(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'number_rooms'))

    def test_number_rooms_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.number_rooms, int)

    def test_number_bathrooms(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'number_bathrooms'))

    def test_number_bathrooms_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_max_guest(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'max_guest'))

    def test_max_guest_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.max_guest, int)

    def test_price_by_night(self):
        """ checks general doc"""
        self.assertTrue(hasattr(Place, 'price_by_night'))

    def test_price_by_night_type(self):
        """ checks general doc"""
        self.assertIsInstance(Place.price_by_night, int)

    def test_latitude(self):
        """ test for latitude"""
        self.assertTrue(hasattr(Place, 'latitude'))

    def test_latitude_type(self):
        """ test for latitude type"""
        self.assertIsInstance(Place.latitude, float)

    def test_longitude(self):
        """ check for longitude"""
        self.assertTrue(hasattr(Place, 'longitude'))

    def test_longitude_type(self):
        """ check for longitude type"""
        self.assertIsInstance(Place.longitude, float)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_amenity_ids_type(self):
        """ id type"""
        self.assertIsInstance(Place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
