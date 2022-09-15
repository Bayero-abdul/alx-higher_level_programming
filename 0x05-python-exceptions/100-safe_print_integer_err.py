#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    if isinstance(value, int):
        print("{:d}".format(value))
        return True
    else:
        sys.stderr.write("Exception: Unknown format code 'd' for object of \
type '{}'\n".format(value.__class__.__name__))
