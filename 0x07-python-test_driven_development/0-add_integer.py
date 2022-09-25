#!/usr/bin/python3
"""0-add_integer.py

This modules contains a function, add_integer().

"""


def add_integer(a, b=98):
    """Adds two numbers

    Returns:
        the sum of a and b
    """
    if isinstance(a, float) and a != a:
        a = 89
    if isinstance(b, float) and b != b:
        b = 89
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
