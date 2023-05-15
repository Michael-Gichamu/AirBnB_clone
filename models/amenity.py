#!/usr/bin/python3
"""Creates Amenity Class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
        args:
            name(str): empty string.
    """
    name: str = ""
