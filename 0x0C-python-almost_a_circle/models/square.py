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
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )
