#!/usr/bin/python3
"""Creates a State Class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel.
    """
    name: str = ""
