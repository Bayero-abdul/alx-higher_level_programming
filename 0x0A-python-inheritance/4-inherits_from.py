#!/usr/bin/python3
"""Module contains ``inherits_from()``"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and issubclass(obj, a_class)
