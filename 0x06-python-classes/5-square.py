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
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = int(size)

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with value"""
        try:
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = int(value)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
