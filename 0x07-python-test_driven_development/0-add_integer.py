#!/usr/bin/python3
"""0-add_integer.py

This modules contains a function, add_integer().

"""


def add_integer(a, b=98):
    """Adds two numbers

    Returns:
        the sum of a and b
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")

    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
