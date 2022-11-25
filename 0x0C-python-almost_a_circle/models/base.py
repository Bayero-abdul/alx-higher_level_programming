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
            self.id = Base.__nb_objects

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
            if not list_objs:
                f.write('[]')
            else:
                my_list = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation."""

        if not json_string: 
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set."""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls == Rectangle:
            dummy = Rectangle(10, 10)
        else:
            dummy = Square(10)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances."""

        try:
            filename = cls.__name__ + '.' + "json"
            with open(filename, 'r', encoding='utf-8') as f:
                new_list = []
                iter_list = cls.from_json_string(f.read())
                for obj_dict in iter_list:
                    new_list.append(cls.create(**obj_dict))
                return new_list

        except FileNotFoundError:
            return []
