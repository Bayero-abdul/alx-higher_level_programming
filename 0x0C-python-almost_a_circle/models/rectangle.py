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

    def area(self):
        """return area of a rectangle."""

        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #."""

        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation."""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""

        if args:
            print("i am args")
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""

        new_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return new_dict
