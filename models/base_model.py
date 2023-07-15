#!/usr/bin/python3

"""
Description: This module contains our base model class.
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel():
    """
    class:
        BaseModel

    attribute:
        1.id: string - assign with an uuid when an instance is created
        2.created_at: assign with the current datetime created
        3.updated_at: datetime - updated every time you change your object
    methods:
        1.save: updates the public instance attribute current datetime.
        2.to_dict: returns a dictionary containing all keys.
        3. Args:
            *args: Unused
            **Kwargs: Key/value pairs of attributes.
    """


    def __init__(self, *args, **kwargs):
        if kwargs:
            exclude_keys = ['__class__']
            for key, value in kwargs.items():
                if key not in exclude_keys:
                    if key == 'created_at' or key == 'updated_at':
                        value = \
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
                        self.__class__.__name__,
                        self.id,
                        self.__dict__
                    )

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Description: a dictionary representation of BaseModel.

        Returns:
            dict: Dictionary containing all keys/values of
                  __dict__ .
                  the __class__ key with the class name.
                  The created_at and updated_at attributes are converted
                  to string objects in ISO format.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
