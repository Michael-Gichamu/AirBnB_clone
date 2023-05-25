#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testuser(unittest.TestCase):
    """Unittest"""
    def test_User(self):
        """
        Test Class User.
        """
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

"""Test suite for the User class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        user = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        user = User()
        self.assertIs(type(user.first_name), str)
        self.assertIs(type(user.last_name), str)
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))
