#!/usr/bin/python3
"""Module contains ``class BaseGeometry``"""


class BaseGeometry:
    """Defines BaseGeometry"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise an error if value is not an integer or
less than or equal to zero"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
