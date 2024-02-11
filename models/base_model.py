#!/usr/bin/python3
"""This module defines a BaseModel class
 that serves as a base class for other classes.
 It provides methods for initializing object instances, 
 converting objects to strings, saving objects, and
 converting objects to dictionary representations."""
import uuid
from datetime import datetime
import models

class BaseModel:
    """This class initializes objects with unique identifiers
    and date-time attributes, allowing for string
    conversion and dictionary representation of
    objects"""
    def __init__(self, *args, **kwargs):
        """Initialization method that
        method call during instanciation"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation method according to
        the rule of the project"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime
        and save it also in the object storage"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """Return dictionary representation of instance
        after copy the attributes to the variable new_dict"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

