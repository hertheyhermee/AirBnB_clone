#!/usr/bin/python3
"""
Description: This module
    serializes instances to a JSON file and deserializes JSON file to instances
"""
import json
import os

class FileStorage():

    __file_path = "file.json"
    _objects = {}


    def all(self):
        """Returns the dict of _objects"""
        return FileStorage._objects

    def new(self, obj):
        FileStorage._objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    # def save(self):
    #     with open(FileStorage.__file_path, "w", encoding="utf-8") as newFile
