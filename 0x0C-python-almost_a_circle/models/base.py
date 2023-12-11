#!/usr/bin/python3

"""0. If it's not tested it doesn't work"""


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
