#!/usr/bin/python3

"""function that prints a square with the character #."""


def print_square(size):
    """prints a square with the character #

    args:
    size (int): size is the size length of the square
    """
    if not isinstance(size, (int, float)) or (size < 1 and size > 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
