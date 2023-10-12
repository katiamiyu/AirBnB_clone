#!/usr/bin/python3
"""
module contain file storage class
"""
import json


class FileStorage:
    """
    class for serializing json string/objects
    file_path private class attribute
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns a dictionary object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        creates a new obj attribute
        update objects class attribute
            Args:
                obj - object instance
        """
        key = (f"{obj.__class__.__name__}.{obj.id}")
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save obj to data file
        """
        obj_dict = {}
        for k, v in FileStorage.__objects.items():
            obj_dict[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        repopulates the __objects object
        """
        from models.base_model import BaseModel
        try:
            with open(__file_path, "r") as f:
                obj_dict = json.loads(f.read())
                for k, v in obj_dict.items():
                    FileStorage.__objects[key] = BaseModel(**v)
        except Exception:
            pass
