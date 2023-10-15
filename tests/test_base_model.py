#!/usr/bin/python3
"""
tests module for basemodel
"""

import unittest
import json
import uuid as generate_id
from models.base_model import BaseModel
from datetime import datetime


global_update = None


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel
    """

    def test_uuid_if_unique(self):
        """
        test for uuid
        """
        new_instance = BaseModel()
        uuid = new_instance.id
        self.assertNotEqual(uuid, str(generate_id.uuid4()))

    def test_attr_presence(self):
        """
        test for attributes
        """
        obj = BaseModel()
        attributes = ["id", "created_at", "updated_at", "to_dict", "save"]
        self.assertTrue(all(hasattr(obj, attr) for attr in attributes))

    def test_date_values(self):
        """
        test for values
        """
        new_instance = BaseModel().to_dict()
        newtime = new_instance["created_at"][:20]
        self.assertEqual(newtime, str(datetime.now().isoformat())[:20])

    def test_str_represtation(self):
        """
        test class string representation
        """
        new_instance = BaseModel()
        self.assertIsInstance(new_instance.__str__(), str)

    def test_save_method(self):
        """
        test the save method
        """
        instance = BaseModel()
        time = instance.created_at
        self.assertEqual(time, instance.updated_at)
        instance.save()
        self.assertNotEqual(time, instance.updated_at)

    def test_init_with_kwargs(self):
        """
        test initialization using kwargs
        """
        test_uuid = "{}".format(generate_id.uuid4())
        string_date_format = "{}".format(datetime.now().isoformat())
        unformatted_date = datetime.fromisoformat(string_date_format)
        raw_data = {
            "__class__": "BaseModel",
            "updated_at": string_date_format,
            "created_at": string_date_format,
            "id": test_uuid
            }
        new_instance = BaseModel(**raw_data)
        self.assertEqual(new_instance.id, test_uuid)
        self.assertEqual(new_instance.updated_at, unformatted_date)
        self.assertEqual(new_instance.created_at, unformatted_date)

    def test_none(self):
        """
        test for when none is passed in as a parameter
        """
        instance = BaseModel(None)
        attributes = ["id", "created_at", "updated_at", "to_dict", "save"]
        self.assertTrue(all(hasattr(instance, attr) for attr in attributes))


if __name__ == "__main__":
    unittest.main()
