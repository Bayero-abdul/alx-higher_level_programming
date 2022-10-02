#!/usr/bin/python3
"""Module contain a rebel class"""


class MyInt(int):
    """Inverts the == and != operations"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
