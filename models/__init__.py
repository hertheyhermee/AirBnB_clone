#!/usr/bin/python3
"""
Package: models
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel,
           # "User": User,
           # "Place": Place,
           # "State": State,
           # "City": City,
           # "Amenity":Amenity,
           # "Review": Review
           }
storage = FileStorage()
storage.reload()
