#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square

    Attributes:
    __size : private square size
    """
    def __init__(self, size=0, position=(0, 0)):
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

        if len(position) != 2 or isinstance(position, tuple) == 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Return the postion of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with value"""
        self.__position = int(value)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                print("#" * self.__size)
