#!/usr/bin/python3
"""
This module contains a "class Square"
definition"""


class Square:
    """Square is a class that defines a square."""

    def __init__(self, size=0):
        """Initializes an objects value to a variable

        Args:
            size (int): size of the square.

        """
        self.size = size

    @property
    def size(self):
        """size is a method which is used for getting the value size."""
        return self.__size

    @size.setter
    def size(self, size):
        """size is a method which sets the value size
        to the private size variable."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area."""
        return self.size**2

    def __add__(self, other):
        """Adds two square objects"""
        return self.area() + other.area()

    def __le__(self, other):
        """check if self is less than or equal to other"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """check if self is greater than or equal to other"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Check if objects are equal"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if objects are not equal"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Checks if self is less than other"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Checks if self is greater than other"""
        return self.area() > other.area()
