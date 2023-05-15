#!/usr/bin/python3
"""Creates a User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
