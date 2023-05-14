import unittest
import os
from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_new_object(self):
        state = State()
        self.storage.new(state)
        all_objects = self.storage.all()
        print(all_objects)
        self.assertEqual(len(all_objects), 1)
        self.assertIn(state, all_objects.values())

    def test_save_reload(self):
        state = State()
        self.storage.new(state)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        print(all_objects)
        self.assertEqual(len(all_objects), 2)
        self.assertIn(state, all_objects.values())


if __name__ == '__main__':
    unittest.main()
