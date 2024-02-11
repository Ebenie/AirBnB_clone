#!/usr/bin/python3
"""tests the file_storage module"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertNotEqual(self.storage.all(), {})
        obj = BaseModel()
        self.storage.new(obj)
        self.assertNotEqual(self.storage.all(), {'BaseModel.' + obj.id: obj})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertNotEqual(self.storage._FileStorage__objects, {'BaseModel.' + obj.id: obj})

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", mode="r", encoding="utf-8") as f:
            saved_data = json.load(f)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, saved_data)
        expected_content = obj.to_dict()
        self.assertEqual(saved_data[key], expected_content)

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, new_storage.all())
        reloaded_obj = new_storage.all()[key]
        self.assertEqual(reloaded_obj.to_dict(), obj.to_dict())

if __name__ == '__main__':
    unittest.main()

