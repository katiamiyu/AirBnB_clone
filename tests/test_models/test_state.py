#!/usr/bin/python3
'''Test module for state class
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    ''''Test class for state
    '''
    def setUp(self):
        '''Sets up state object
        '''
        self.state1 = State()
        self.state1.save()

    def test_inherit_BaseModel(self):
        '''Test if state inherites base_model
        '''
        self.assertIsInstance(self.state1, BaseModel)

    def test_attr_name(self):
        '''Test if state class has name
        '''
        self.assertTrue(hasattr(State, "name"))

    def test_name_type(self):
        '''Tests the type of the name
        '''
        self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
