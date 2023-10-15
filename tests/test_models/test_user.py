#!/usr/bin/python3
'''tests for user
'''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''Tests class for User class
    '''

    def setUp(self):
        '''Sets up variables
        '''
        self.my_user = User()
        self.my_user.save()

    def test_user_inherits_from_basemodel(self):
        '''Tests User class inherits from BaseModel
        '''
        self.assertIsInstance(self.my_user, BaseModel)

    def test_email(self):
        '''Tests for email attribute
        '''
        self.assertTrue(hasattr(User, 'email'))

    def test_email_type(self):
        '''Test for email attribute type
        '''
        self.assertIsInstance(User.email, str)

    def test_password(self):
        '''Tests that User has password attribute
        '''
        self.assertTrue(hasattr(User, 'password'))

    def test_password_type(self):
        '''Test for password attribute type
        '''
        self.assertIsInstance(User.password, str)

    def test_first_name(self):
        '''Tests that User has first_name
        '''
        self.assertTrue(hasattr(User, 'first_name'))

    def test_first_name_type(self):
        '''Test for first_name attribute type
        '''
        self.assertIsInstance(User.first_name, str)

    def test_last_name(self):
        '''Tests if User object has last_name attribute
        '''
        self.assertTrue(hasattr(User, 'last_name'))

    def test_last_name_type(self):
        '''Test for last_name attribute type
        '''
        self.assertIsInstance(User.last_name, str)


if __name__ == "__main__":
    unittest.main()
