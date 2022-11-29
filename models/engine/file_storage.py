#!/usr/bin/python3
""" File Storage Module """
import json


class FileStorage:
    """
    class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fil:
            json.dump(FileStorage.__objects, fil)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fil:
                FileStorage.__objects = json.load(fil)
        except Exception:
            pass
