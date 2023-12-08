#!/usr/bin/python3

"""appends a string at the end"""


def append_write(filename="", text=""):
    """append a string to a text file (UTF-8).

    args:
    filename: The name of the file to be written.
    text: The string to be written to the file.

    return: The number of characters added.
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)

        return len(text) + text.count("\n") + text.count(" ")
