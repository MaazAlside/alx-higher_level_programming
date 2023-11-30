#!/usr/bin/python3

"""Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle Class take width and hight args

    args:
    width (int): Private instance attribute
    height (int): Private instance attribute

    """
    def __init__(self, width=0, height=0):
        """Set the values"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieve the height value"""
        return self.__height

    @property
    def width(self):
        """Retrieve the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set The value with new value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Set the the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Method returns the rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += "#" * self.width
            if i < self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
