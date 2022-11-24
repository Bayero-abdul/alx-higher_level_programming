#!/usr/bin/python3
"""This module contains a `Square class`.

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from the Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance."""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}"

    @property
    def size(self):
        """gets the size."""

        return self.width

    @size.setter
    def size(self, val):
        """sets the value of size."""

        if type(val) is not int:
            raise TypeError("width must be an integer")

        if val <= 0:
            raise ValueError("width must be > 0")

        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""

        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
