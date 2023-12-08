#!/usr/bin/python3

"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    args:
    filename: The name of the JSON file.

    Return:
    The Python object.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
