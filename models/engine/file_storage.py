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
    def __init__(self):
        """ initialises instance attributes """
        pass

    def all(self):
        """ returns dictionary __objects """
        return type(self).__objects

    def new(self, obj):
        """
        sets in __objects the object with key <obj class name>.id
        Attributes:
            obj: <obj class name>.id
        """
        key = {}.{}.format(obj.__class__.__name__,obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path """
        with open(__file_path, "w") as write_file:
            json.dump(__objects, write_file)

    def reload(self):
        """ deserializes json file to __objects """
        if __file_path:
            with open(__file_path, "r") as read_file:
                __objects = json.load(read_file)
