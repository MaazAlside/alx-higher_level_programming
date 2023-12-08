#!/usr/bin/python3

"""Read the content of a file and print it."""


def read_file(filename=""):
    """
    Read the content of a file and print it.

    :param filename: The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read())
