#!/usr/bin/python3

"""Function that adds 2 integers.
This module provides a function, add_integer, that can be used to add two integers.
It ensures that the input parameters are either integers or floats, and then returns
the sum of the two numbers. The function also has default values for the second parameter.
"""

def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
        int: The sum of the two input numbers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    """
    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
