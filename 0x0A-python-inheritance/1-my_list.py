#!/usr/bin/python3

class MyList(list):
    """
    MyList is a custom class that extends the built-in list class.

    This class provides additional functionality for working with lists.

    Attributes:
        No additional attributes are defined.

    Methods:
        __init__: Initializes an instance of the MyList class.
        print_sorted: Prints the elements of the list in sorted order.
    """

    def __init__(self):
        """
        Initialize an instance of the MyList class.

        Parameters:
            *args: Variable-length argument list,
            allowing the initialization of the list with values.

        Returns:
            None
        """
        super(MyList, self).__init__()

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        Parameters:
            None

        Returns:
            None
        """
        sortedlist = sorted(self)
        print(sortedlist)
