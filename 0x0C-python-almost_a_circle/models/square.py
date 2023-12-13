#!/usr/bin/python3
"""10. And now, the Square!"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle.

    Attributes:
        size (int): Size of the square.
        x (int): x-coordinate of the square's position.
        y (int): y-coordinate of the square's position.
        id (int): Optional ID for the instance.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square's position.
            y (int): y-coordinate of the square's position.
            id (int): Optional ID for the instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )

    def update(self, *args, **kwargs):
        """Update the class Square attributes

        Args:
            *args: A variable number of arguments representing the attributes
                   in the following order: id, size, x, y.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
