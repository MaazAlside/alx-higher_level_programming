#!/usr/bin/python3
def no_c(my_string):
    new_string = [letter for letter in my_string
                  if letter != "C" and letter != "c"]
    return "".join(new_string)
