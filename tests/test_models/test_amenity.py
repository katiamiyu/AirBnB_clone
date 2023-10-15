#!/usr/bin/python3
"""
test class for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    defines tests for Amenity objects
    """

    def test_inherits_BaseModel(self):
        """test for inheritance """
        self.test_amenity = Amenity()
        self.assertIsInstance(self.test_amenity, BaseModel)

    def test_name(self):
        """ test for attribute"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_name_type(self):
        """ test for attribute type"""
        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
