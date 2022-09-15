#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        sys.stderr.write("Exception: Unknown format code 'd' for object of \
type '{}'\n".format(value.__class__.__name__))
        return False
