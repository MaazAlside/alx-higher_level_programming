#!/usr/bin/python3

""" function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object to inspect.

    Returns:
    list: A list of strings of attributes and methods of the object.
    """
    return dir(obj)
