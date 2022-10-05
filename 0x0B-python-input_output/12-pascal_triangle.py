#!/usr/bin/python3
"""Module contain ``pascal_triangle()``"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the \
    Pascals triangle of n"""

    if n <= 0:
        return []

    pascal_lst = [[1]]
    while len(pascal_lst) != n:
        prev_lst = pascal_lst[-1]
        lst = [1]
        for i in range(len(prev_lst) - 1):
            lst.append(prev_lst[i] + prev_lst[i + 1])
        lst.append(1)
        pascal_lst.append(lst)
    return pascal_lst
