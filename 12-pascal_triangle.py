#!/usr/bin/python3
"""Module contain ``pascal_triangle()``"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the \
    Pascals triangle of n"""
    pascal_lst = []
    for i in range(n):
        if i == 0:
            pascal_lst.append([1])
            continue
        lst = []
        lst_len = i + 1
        for j in range(lst_len):
            prev_lst = pascal_lst[i - 1]
            if j == 0:
                lst.append(1)
                continue
            if j == 1 and len(prev_lst) == 1:
                lst.append(1)
                break

            if j >= ((lst_len // 2) + 1):
                lst.append(lst[abs(j - (lst_len - 1))])
                continue
            if j < len(prev_lst):
                lst.append(prev_lst[j - 1] + prev_lst[j])
        pascal_lst.append(lst)
    return pascal_lst
