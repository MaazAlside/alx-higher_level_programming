#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square

    Attributes:
        __size (int): the size of Square.
        __position (tuple): The position of the square.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): the size of the Square.
            position (tuple): The position of the square.
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = int(size)
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
        """Return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with value"""
        if not isinstance(value, tuple) or len(value) != 2 \
            or not all(isinstance(i, int) for i in value) \
                or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
