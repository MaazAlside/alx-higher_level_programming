#!/usr/bin/python3

"""function that returns True if the object is
exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """Fuction check the type of object

    args:
    ogj: opject to check
    a_class: class to check the object
    """
    return type(obj) is a_class
