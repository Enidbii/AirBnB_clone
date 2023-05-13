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

    def __init__(self, *args, **kwargs):
        """
        It initialises the basemodel class

        Attributes:
            *args: variable number of arguments to be passed
            **kwargs: variable no of dictionaries to be passed

        """
        if kwargs:
            dateobject = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        dateobject)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        dateobject)
                else:
                    setattr(self, key, value)
        else:
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

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
#print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
