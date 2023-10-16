#!/usr/bin/python3
"""
test file for file_storage
"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test class for file_storage"""

    def setUp(self):
        """ create obj for use"""
        self.obj = FileStorage()

    def test_attr_presence(self):
        """ test attr presence"""
        attr_list = ["all", "new", "save", "reload", "destroy"]
        self.assertTrue(all(hasattr(self.obj, attr) for attr in attr_list))

    def test_instance(self):
        """ check object insyance"""
        self.assertIsInstance(self.obj, FileStorage)

    def test_attr_all(self):
        """ test for object method all"""
        result = self.obj.all()
        self.assertIsInstance(result, dict)

    def test_attr_new(self):
        pass

    def test_attr_save(self):
        pass

    def test_attr_reload(self):
        pass

    def test_attr_destroy(self):
        pass


if __name__ == "__main__":
    unittest.main()
