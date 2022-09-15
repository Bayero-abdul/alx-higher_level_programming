#!/usr/bin/python3
"""
This module contains a "class Square"
definition"""


class Square:
    """Square is a class that defines a square."""

    def __init__(self, size=0, postion=(0, 0)):
        """Initializes an objects value to a variable

        Args:
            size (int): size of the square.
            position (tuple): 

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

    def my_print(self):
        if self.size == 0:
            print()

        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
