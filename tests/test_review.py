#!/usr/bin/python3
'''Module tests for the `Review` class
'''
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    '''Test for Review class
    '''

    def test_inherits_BaseModel(self):
        '''Test for inheritance
        '''
        self.test_review = Review()
        self.assertIsInstance(self.test_review, BaseModel)

    def test_place_id(self):
        '''Test for place id
        '''
        self.assertTrue(hasattr(Review, 'place_id'))

    def test_place_id_type(self):
        '''Test for place id type
        '''
        self.assertIsInstance(Review.place_id, str)

    def test_user_id(self):
        '''Test for user_id
        '''
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_user_id_type(self):
        '''Test for user id type
        '''
        self.assertIsInstance(Review.user_id, str)

    def test_text(self):
        '''Test for text
        '''
        self.assertTrue(hasattr(Review, 'text'))

    def test_text_type(self):
        '''Test for text type
        '''
        self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
