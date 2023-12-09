#!/usr/bin/python3
"""
Correction of "7. Integer validator
"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def area(self):
        """area not emplemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value

        args:
        name: is always a string
        value: is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
