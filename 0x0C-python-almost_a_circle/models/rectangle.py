#!/usr/bin/python3

"""A class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle, inheriting from the Base class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): An optional ID for the instance.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
