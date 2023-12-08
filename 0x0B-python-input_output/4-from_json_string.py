#!/usr/bin/python3

"""returns the object representation of JSON"""
import json


def from_json_string(my_str):
    """
    Convert a JSON representation to  Python object.

    args
    obj: The Python object to be converted.

    Return
    The JSON-formatted string.
    """
    return json.loads(my_str)
