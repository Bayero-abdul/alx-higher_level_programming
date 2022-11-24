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
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation."""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
