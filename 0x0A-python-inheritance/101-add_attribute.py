#!/usr/bin/python3
"""Module contain ``add_attribute()`` function"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if its possible"""
    if getattr(obj, '__dict__', 0) == 0:
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
