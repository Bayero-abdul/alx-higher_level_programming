#!/usr/bin/python3
"""This module contains a `Rectangle class`.

"""

from models.base import Base


class Rectangle(Base):
    """Inherits from the Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance."""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width."""

        return self.__width

    @width.setter
    def width(self, val):
        """sets the value of width."""

        self.__width = val

    @property
    def height(self):
        """gets the height."""

        return self.__height

    @height.setter
    def height(self, val):
        """sets the value of height."""

        self.__height = val

    @property
    def x(self):
        """gets the x."""

        return self.__x

    @x.setter
    def x(self, val):
        """sets the value of x."""

        self.__x = val

    @property
    def y(self):
        """gets the y."""

        return self.__y

    @y.setter
    def y(self, val):
        """sets the value of y."""

        self.__y = val
