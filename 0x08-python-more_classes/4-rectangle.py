#!/usr/bin/python3
"""Module contains a Rectangle class definition."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Iniatializes instances variables."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """retuns the string representation of a class"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for i in range(self.height):
                for j in range(self.width):
                    result += '#'
                if i != self.height - 1:
                    result += '\n'
            return result

    def __repr__(self):
        """returns formal string representation"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
