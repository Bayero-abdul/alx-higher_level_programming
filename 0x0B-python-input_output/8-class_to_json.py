#!/usr/bin/python3
"""Module contain ``class_to_json()`` function"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure \
    for JSON serialization of an object"""
    return obj.__dict__
