#!/usr/bin/python3

"""function that print full name"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    args:
    first_name: first name arg
    last_name: opional last name arg

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
