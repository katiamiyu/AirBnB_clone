#!/usr/bin/python3
"""
test for city class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ test"""
    def setUp(self):
        self.city1 = City()
        self.city1.save()

    def test_inherit_BaseModel(self):
        """ check for inheritance"""
        self.assertIsInstance(self.city1, BaseModel)

    def test_has_name(self):
        """ check name attr"""
        self.assertTrue(hasattr(City, "name"))

    def test_name_type(self):
        """ test name type"""
        self.assertIsInstance(City.name, str)

    def test_has__state_id(self):
        """ check state id"""
        self.assertTrue(hasattr(City, "state_id"))

    def test_state_id_type(self):
        """ check state id type"""
        self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
