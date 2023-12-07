#!/usr/bin/python3

"""an empty class """


class BaseGeometry:
    """Empty Class """

    def __init__(self):
        """inilize the opject"""
        pass

    def area(self):
        """area not emplemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value

        args:
        name: is always a string
        value: is less or equal to 0
        """

        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
