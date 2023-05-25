#!/usr/bin/python3
"""
Defines BaseModel Class.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    Base Class for all models.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization of a Base instance.

        Args:
            args: list of arguemnts.
            kwargs: dict of key-value arguments.
        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def save(self):
        """
        Updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary that contains all key/values
        of the instance.

        """
        dict_ = dict(self.__dict__)
        dict_['__class__'] = self.__class__.__name__
        dict_['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_

    def __str__(self):
        """
        String representation of instance.
        """
        class_name = self.__class__.__name__
        return "[{:s}] ({:s}) {}".format(class_name, self.id, self.__dict__)
