#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:

        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                       'M': 1000}
        total_value = 0
        prev_value = 0

        for char in roman_string:
            current_value = roman_value[char]
            if current_value > prev_value:
                total_value += current_value - 2 * prev_value
            else:
                total_value += current_value
            prev_value = current_value

        return total_value
    else:
        return 0
