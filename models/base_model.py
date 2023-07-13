from datetime import datetime
from uuid import uuid4

"""
This module contains our base model class.
class:
    BaseModel

attribute:
    1.id: string - assign with an uuid when an instance is created
    2.created_at: assign with the current datetime when an instance is created
    3.updated_at: datetime - updated every time you change your object
methods:
    1.save: updates the public instance attribute updated_at with the current datetime.
    2.to_dict: returns a dictionary containing all keys/values of __dict__ of the instance.
"""
class BaseModel():


    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[<class name>] (<self.id>) <self.__dict__>".format(name,id,self.__dict__)
