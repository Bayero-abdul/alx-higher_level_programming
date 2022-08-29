#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    first_elem = 0
    second_elem = 0

    if tuple_a == () and tuple_b == ():
        first_elem = 0
        second_elem = 0
    elif tuple_a == ():
        first_elem = tuple_b[0]
        second_elem = tuple_b[1]
    elif tuple_b == ():
        first_elem = tuple_a[0]
        second_elem = tuple_a[1]

    elif len(tuple_a) < 2 and len(tuple_b) < 2:
        if tuple_a[0] is None and tuple_b[0] is None:
            first_elem = 0 + 0
        elif tuple_a[0] is None and tuple_b[0] is not None:
            first_elem = 0 + tuple_b[0]
        else:
            first_elem = tuple_a[0]

        if tuple_a[1] is None and tuple_b[1] is None:
            second_elem = 0
        elif tuple_a[1] is None and tuple_b[1] is not None:
            second_elem = tuple_b[1]
        else:
            second_elem = tuple_a[1]
    elif len(tuple_a) < 2:
        if tuple_a[0] is None:
            first_elem = tuple_b[0]
            second_elem = tuple_a[1] + tuple_b[1]
        else:
            first_elem = tuple_a[0] + tuple_b[0]
            second_elem = tuple_b[1]
    elif len(tuple_b) < 2:
        if tuple_b[0] is None:
            first_elem = tuple_a[0]
            second_elem = tuple_a[1] + tuple_b[1]
        else:
            first_elem = tuple_a[0] + tuple_b[0]
            second_elem = tuple_a[1]
    else:
        first_elem = tuple_a[0] + tuple_b[0]
        second_elem = tuple_a[1] + tuple_b[1]

    return((first_elem, second_elem))
