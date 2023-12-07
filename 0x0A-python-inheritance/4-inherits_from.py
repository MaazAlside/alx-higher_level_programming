#!/usr/bin/python3

"""
Returns True if the object is an instance of a class that inherited
(directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """fuction check if the object is an instance of a class that inherited

    args:
    obj: object
    a_class: class
    """
    return a_class != type(obj)
