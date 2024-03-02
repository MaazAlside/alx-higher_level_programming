#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    for i in range(n):
        if list_of_integers[i] >= list_of_integers[i + 1] and \
           list_of_integers[i] >= list_of_integers[i - 1]:
            return list_of_integers[i]
