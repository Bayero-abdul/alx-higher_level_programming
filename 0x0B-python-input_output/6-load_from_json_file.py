#!/usr/bin/python3
"""Module contain ``from_to_json_file()`` function"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        import json
        return json.loads(f.read())
