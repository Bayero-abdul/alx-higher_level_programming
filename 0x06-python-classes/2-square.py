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
        if type(size) != "int":
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
