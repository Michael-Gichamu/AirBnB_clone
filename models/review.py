#!/usr/bin/python3
"""Creates a Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    
    args:
        place_id (str): The ID of the place. Defaults to an empty string, which will be the Place.id.
        user_id (str): The ID of the User. Defaults to an empty string, which will be the User.id.
        text (str): Empty string.
    """
    place_id = ""
    user_id = ""
    text = ""
