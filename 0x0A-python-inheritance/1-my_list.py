#!/usr/bin/python3

"""class MyList that inherits from list"""


class MyList(list):
    """
    MyList is a custom class that extends the built-in list class.

    This class provides additional functionality for working with lists.

    Attributes:
        No additional attributes are defined.

    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        Parameters:
            None

        Returns:
            None
        """
        print(sorted(self))
