#!/usr/bin/python3
"""Creates a City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
        args:
            state_id (str): empty string: it will be the State.id.
            name (str): empty string.
    """
    state_id = ""
    name = ""
