#!/usr/bin/python3
"""Module contains ``inherits_from()``"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class"""
    return issubclass(obj, a_class) and type(obj) != a_class
