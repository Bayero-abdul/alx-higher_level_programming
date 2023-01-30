#!/usr/bin/python3
"""Module contain a lookup() function."""


def lookup(obj):
    """returns the list of available attributes and methods of an object."""
    if isinstance(obj, object):
        return dir(obj)
