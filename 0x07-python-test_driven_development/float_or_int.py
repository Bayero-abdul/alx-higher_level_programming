#!/usr/bin/python3
def int_or_float(a , b):
    """Return 1 if a and b is a float or int,
    else returns 0.

    Works with numbers:

    >>> int_or_float(3, 5)
    1

    >>> int_or_float(5.3, 6)
    1

    >>> int_or_float(-6, -6.5)
    1

    >>> int_or_float(5.2, 4.3)
    1

    and other types:

    >>> int_or_float(3, "hello")
    0

    >>> int_or_float(None)
    0

    >>> int_or_float()
    0

    >>> int_or_float(3.5, "i")
    0

    >>> int_or_float([1, 2], "chiccha")
    0

    >>> int_or_float([1,3], 5)
    0
    """
    if a is not None or b is not None:
        if (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float):
            return 1
    return 0
