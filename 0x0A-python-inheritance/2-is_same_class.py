#!/usr/bin/python3
"""Module contains ``class is_same_class``"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an
instance of the specified c"""
    if type(obj) is a_class:
        return True
    else:
        return False
