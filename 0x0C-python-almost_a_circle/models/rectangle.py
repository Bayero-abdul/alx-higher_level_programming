#!/usr/bin/python3
"""This module contains a `Rectangle class`.

"""

from models.base import Base


class Rectangle(Base):
    """Inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance."""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width."""

        return self.__width

    @width.setter
    def width(self, val):
        """sets the value of width."""

        if type(val) != int:
            raise TypeError("width must be an integer")

        if val <= 0:
            raise ValueError("width must be > 0")

        self.__width = val

    @property
    def height(self):
        """gets the height."""

        return self.__height

    @height.setter
    def height(self, val):
        """sets the value of height."""

        if type(val) is not int:
            raise TypeError("height must be an integer")

        if val <= 0:
            raise ValueError("height must be > 0")

        self.__height = val

    @property
    def x(self):
        """gets the x."""

        return self.__x

    @x.setter
    def x(self, val):
        """sets the value of x."""

        if type(val) != int:
            raise TypeError("x must be an integer")

        if val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    @property
    def y(self):
        """gets the y."""

        return self.__y

    @y.setter
    def y(self, val):
        """sets the value of y."""

        if type(val) != int:
            raise TypeError("y must be an integer")

        if val < 0:
            raise ValueError("y must be >= 0")

        self.__y = val
