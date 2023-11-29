#!/usr/bin/python3

"""Function that adds 2 integers.
This module provides a function, add_integer,
that can be used to add two integers.
example 3 + 2 return 5
"""


def add_integer(a, b=98):
    """Function that adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
