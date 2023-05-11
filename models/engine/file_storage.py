#!/usr/bin/python3
"""
Defines FileStorage class.
"""
import json
import os.path
from models.base_model import BaseModel


class FileStorage:
    """
    Represents File storage class.
    Args:
        __file_path (string): path to the Json file.
        __objects (dictionary): empty but will store
                                all objects by <class name>.id

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        dict_key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({dict_key: obj})

    def save(self):
        """ serializes __objects to the JSON file """
        dict_ = {}
        for key in self.__objects:
            dict_[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dict_, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_obj = json.load(file)
            for key, value in json_obj.items():
                class_name = value['__class__']
                self.__objects[key] = eval(class_name)(**value)
