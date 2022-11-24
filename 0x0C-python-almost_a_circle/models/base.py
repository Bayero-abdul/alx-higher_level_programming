#!/usr/bin/python3
"""This module contains a `Base class`.

"""

import json


class Base:
    """Base of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance."""

        if type(id) is int:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation."""

        if not list_dictionaries:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
