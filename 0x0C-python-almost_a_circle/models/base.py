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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file."""

        filename = cls.__name__ + '.' + 'json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(my_list))
