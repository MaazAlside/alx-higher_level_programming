#!/usr/bin/python3

"""0. If it's not tested it doesn't work"""
import json


class Base:
    """Base class for other classes in the module."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): An optional ID for the instance. If not provided,
                      a default ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON-formatted string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        fname = cls.__name__ + ".json"
        with open(fname, 'w') as file:
            file.write(
                    cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs]
                        if list_objs
                        else [])
                    )

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON-formatted string to list represented """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_instance = cls(1, 10,  x=5, y=6)
        dummy_instance.update(**dictionary)
        return dummy_instance
