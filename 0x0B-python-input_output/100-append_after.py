#!/usr/bin/python3
"""Module contain ``append_after()`` function that \
that inserts a line of text to a file, after each line \
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line \
        containing a specific string"""

    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        f.truncate(0)
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
