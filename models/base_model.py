#!/usr/bin/python3
"""
Defines BaseModel Class.
"""
from datetime import datetime
import uuid
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
        if kwargs:
            Tformat = "%Y-%m-%dT%H:%M:%S.%f"
            if "created_at" in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], Tformat)
            if "updated_at" in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], Tformat)
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

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
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
