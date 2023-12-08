#!/usr/bin/python3

import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation.

    args
    obj: The Python object to be converted.

    Return
    The JSON-formatted string.
    """
    return json.dumps(my_obj)
