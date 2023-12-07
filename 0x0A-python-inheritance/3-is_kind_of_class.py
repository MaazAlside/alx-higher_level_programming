#!/usr/bin/python3

"""Determine if the object is an instance or subclass of
the specified class; return True or False accordingly"""


def is_kind_of_class(obj, a_class):
    """
    Check if object is instance or subclass.

    args:
    obj: object to check
    a_class: class to check
    """
    return isinstance(obj, a_class)
