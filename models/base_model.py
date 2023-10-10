#!/usr/bin/python3
"""
module
contains the base model of Airbnb app
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    this is the base class for other classes
   """

    def __init__(self, *args, **kwargs):
        """
        this function initialises each instance
        whem created.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        returns the string representation of an
        instance object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates the instance attributes
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns the dictionary representation of an instance
        object
        """
        instance_dict = {}
        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                instance_dict[key] = value.isoformat()
            else:
                instance_dict[key] = value
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
