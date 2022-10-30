#!/usr/bin/python3
"""
File Storage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serialiizes and Deserializes JSON files"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns dictionary of <class>.<id> : object instance"""
        return self.__objects

    def new(self, obj):
        """Add new object to existing dictionary of instances"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[keys] = obj

    def save(self):
        """save object dictionary to JSON file"""
        my_dict = {}

        for key, obj in self.__objects.items():
            """
            if type(obj) is dict:
                my_dict[key] = obj
            else:
            """
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Convert object dict back to instances if JSON file exist"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                self.__objects[key] = eval(key.split(".")[0])(**val)
        except FileNotFoundError:
            pass
