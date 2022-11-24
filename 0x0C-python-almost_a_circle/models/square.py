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
