#!/usr/bin/python3
"""2-matrix_divided.py

This modules contains a function, matrix_divided() and
Is_matrix_of_int_float()

"""

def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Returns:
        new matrix of divided elements in the matrix
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not is_matrix_of_int_float(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])
    if (sum([1 for l in matrix if len(l) != length]) >= 1):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in l] for l in matrix]


def is_matrix_of_int_float(matrix):
    """Checks if a matrix is al ist of lists of integers or floats."""

    if type(matrix) != list or matrix == [] or matrix == [[]]:
        return 0

    for l in matrix:
        if type(l) != list:
            return 0
        for num in l:
            if type(num) != int and type(num) != float:
                return 0
    return 1
