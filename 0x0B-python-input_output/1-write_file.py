#!/usr/bin/python3
"""Module contain ``write_file()`` function"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file (UTF8)
and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
