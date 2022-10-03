#!/usr/bin/python3
"""Module contain ``save_to_json_file()`` function"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        import json
        f.write(json.dumps(my_obj))
