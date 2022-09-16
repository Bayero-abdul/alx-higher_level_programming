#!/usr/bin/python3
"""
This module contains a "class Square"
definition"""


class Square:
    """Square is a class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an objects value to a variable

        Args:
            size (int): size of the square.
            position (tuple): position to start printing

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size is a method which is used for getting the value size."""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the value size to the private size variable."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """gets the value of position."""
        return self.__position

    @position.setter
    def position(self, position):
        """sets the value position to the private position variable."""
        if type(position) != tuple or len(position) != 2 or\
                (type(position[0]) != int or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """returns the current square area."""
        return self.size**2

    def my_print(self):
        """ prints a block of # """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
