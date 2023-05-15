#!/usr/bin/python3
"""Creates a User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class
    args:
        email (str): empty string
        password (str): empty string
        first_name (str): empty string
        last_name (str): empty string
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
