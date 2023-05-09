#!/usr/bin/python3
"""
Defines a base model class.
"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    Base Class for all models.
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

    def save(self):
        """
        Updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Return the str() representation of the Basemodel.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
