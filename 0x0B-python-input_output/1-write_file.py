#!/usr/bin/python3

"""function that writes to a text file returns the number of characters"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8)
    and return the number of characters written.

    args:
    filename: The name of the file to be written.
    text: The string to be written to the file.

    return: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

        return len(text) + text.count("\n") + text.count(" ")
