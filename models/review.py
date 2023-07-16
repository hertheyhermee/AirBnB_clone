#!/usr/bin/python3
'''
    Implementation of the Review class
'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Review implementation.
    '''
    place_id = ""
    user_id = ""
    text = ""
