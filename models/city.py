#!/usr/bin/python3
"""Creates a City Class"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """
    state_id: str = ""
    name: str = ""
