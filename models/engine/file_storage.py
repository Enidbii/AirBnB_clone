#!/usr/bin/python3
""" FileStorage module """

import os
import json
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "State": State,
        "Review": Review,
        "Amenity": Amenity
        }


class FileStorage:
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
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path """
        ourdict = []
        for obj in type(self).__objects.values():
            ourdict.append(obj.to_dict())

        with open(type(self).__file_path, "w") as write_file:
            json.dump(ourdict, write_file)

    def reload(self):
        """ deserializes json file to __objects """
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self)__file_path, "r") as read_file:
                    ourdictobj = json.load(read_file)
                    for key, value in ourdictobj.items():
                        obj = self.classes[value['__class__']](**value)
                        type(self).__objects[key] = obj
            except Exception:
                pass
