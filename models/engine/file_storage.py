#!/usr/bin/python3
"""This module defines a class to manage file storage
 for  HBNB clone project, facilitating serialization
 and deserialization of objects to and
 from a JSON file"""
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel

class FileStorage:
    """This class manages the storage of objects
    in a dictionary and handles serialization and 
    deserialization to/from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns all the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    new_obj = BaseModel(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass
