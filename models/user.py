'''
    User class which inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
        Defines the User class
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
