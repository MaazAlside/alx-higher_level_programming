#!/usr/bin/python3

"""

function that prints a text with 2
new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """function that prints a text

    args:
    text: a string massages,
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        line = []
        for char in text:
            if char in ('.', '?', ':'):
                print(f"{char}\n")
                flag = True
            elif char == ' ' and flag:
                continue
            else:
                line.append(char)
                print(char, end="")
                flag = False
