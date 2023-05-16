#!/usr/bin/python3
""" FileStorage module """

import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """
    serializes instances to JSON file and vice versa

    private class attributes:
        __file_path: string file to JSON file
        __objects: dictonary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the object with key <obj class name>.id
        Attributes:
            obj: <obj class name>.id
        """
        key = {}.{}.format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path """
        with open(FileStorage.__file_path, "w") as write_file:
            json.dump(FileStorage.__objects, write_file)

    def reload(self):
        """ deserializes json file to __objects """
        try:
            with open(__file_path, "r", encoding="utf-8") as read_file:
                FileStorage__objects = json.load(read_file)
        except FileNotFoundError:
            pass
