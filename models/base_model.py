#!/usr/bin/python3
""" Base model module: base_model.py
    defines all common attributes/methods for other classes

"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods of other classes

    """

    def __init__(self):
        """
        It initialises the basemodel class

        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        prints the string representation of the class

        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated at to the current
        date time

        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__

        """
        our_dict = self.__dict__
        our_dict["__class__"] = self.__class__.__name__
        our_dict["created_at"] = self.created_at.isoformat()
        our_dict["updated_at"] = self.updated_at.isoformat()
        return our_dict
