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
        if kwargs == 0:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            Tformat = "%Y-%m-%dT%H:%M:%S.%f"
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], Tformat)
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
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Return the string representation of the Basemodel.
        """
        return f "[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

