#!/usr/bin/python3
"""
Description: This module
    serializes instances to a JSON file and deserializes JSON file to instances
"""
from json import dump, load
import models


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dict of _objects"""
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        serial_Obj = {}
        for key, value in FileStorage.__objects.items():
            serial_Obj[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as\
                new_json:
            dump(serial_Obj, new_json)

    def reload(self):
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as new_json:
                FileStorage.__objects = load(new_json)
                for key, value in FileStorage.__objects.items():
                    class_name = value["__class__"]
                    class_name = models.classes[class_name]
                    FileStorage.__objects[key] = class_name(**value)
        except FileNotFoundError:
            pass
