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
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {"BaseModel": BaseModel, "State": State,
                      "City": City, "Amenity": Amenity,
                      "Place": Place, "Review": Review}

        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    obj = class_dict[v["__class__"]](**v)
                    FileStorage.__objects[k] = obj
        except Exception:
            pass

    def destroy(self, obj_key):
        if obj_key in FileStorage.__objects:
            del (FileStorage.__objects[obj_key])
        self.save()
