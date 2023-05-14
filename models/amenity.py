#!/usr/bin/python3

from base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """
    name: str = ""
