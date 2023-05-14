#!/usr/bin/python3
"""
Defines BaseModel Class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class from which future classes will be inherited from
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of a Base instance.

        Args:
            args: list of arguemnts.
            kwargs: dict of key-value arguments.
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            Tformat = "%Y-%m-%dT%H:%M:%S.%f"
            if 'created_at' in kwargs:
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], Tformat)
            if 'updated_at' in kwargs:
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], Tformat)
            for key, value in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, value)

    def save(self):
        """
        Updates the attribute `updated_at` with the current datetime
        """
        self.updated_at = datetime.now()

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

    # def __eq__(self, other):
    #     """
    #     Overrides the default equality comparison between BaseModel objects.
    #     Two BaseModel objects are considered equal if their IDs are the same.
    #     """
    #     return isinstance(other, BaseModel) and self.id == other.id

    def __str__(self):
        """
        Return the string representation of the Basemodel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
