from datetime import now
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
