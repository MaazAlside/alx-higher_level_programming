#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square

    Attributes:
    __size : private square size
    """
    def __init__(self, size=0):
        """Initialize a new Square

        Args:
        size (int): the size of Square
        """
        try:
            self.__size = int(size)
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
