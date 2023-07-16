#!/usr/bin/python3

'''
    Description:
        All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Description:
            Testing Review class
    '''

    def test_Review_inheritance(self):
        '''
            Description:
                tests that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Description:
                Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        '''
            Description:
                Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        Description:
            text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
