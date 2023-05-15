#!/usr/bin/python3
"""Creates a State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    
    args:
        name (str): name of user.
    """
    name: str = ""
