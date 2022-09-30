#!/usr/bin/python3
"""Module contains class MagicClass and
area() and circumference()"""
import math


class MagicClass:
    """Defines MagicClass objects"""
    def __init__(self, radius=0):
        """Initializes values of instances"""
        self._MagicClass__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        return self._MagicClass__radius

    def area(self):
        """returns the area of a circle"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """returns the circumference of a circle"""
        return 2 * math.pi * self._MagicClass__radius
