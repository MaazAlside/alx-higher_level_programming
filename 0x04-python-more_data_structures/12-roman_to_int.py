#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:

        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                       'M': 1000}
        value = 0
        for char in roman_string:
            value += roman_value[char]

        return (value)
    else:
        return (0)
