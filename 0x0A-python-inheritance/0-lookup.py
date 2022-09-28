#!/usr/bin/python3
def lookup(obj):
    if isinstance(obj, object):
        return dir(obj)
