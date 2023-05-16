#!/usr/bin/python3
""" FileStorage module """

import json
import os
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
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the object with key <obj class name>.id
        Attributes:
            obj: <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file(path: __file_path """
        ourdict = FileStorage.__objects
        ourdictobj = {obj: ourdict[obj].to_dict() for obj in ourdict.keys()}
        with open(FileStorage.__file_path, "w") as write_file:
            json.dump(ourdictobj, write_file)

    def reload(self):
        """ deserializes json file to __objects """
        try:
            with open(FileStorage__file_path, "r") as read_file:
                ourdictobj = json.load(read_file)
                for i in ourdictobj.values():
                    name_o_cls = i["__class__"]
                    del i["__class__"]
                    self.new(eval(name_o_class)(**i))
        except FileNotFoundError:
            return
