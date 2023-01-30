#!/usr/bin/python3
""" module contains matrix_mul() function."""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrice"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    if not is_matrix(m_a):
        raise TypeError("m_a must be a list of lists")
    if not is_matrix(m_b):
        raise TypeError("m_b must be a list of lists")

    if is_empty(m_a):
        raise ValueError("m_a can't be empty")
    if is_empty(m_b):
        raise ValueError("m_b can't be empty")

    if not is_matrix_of_floats_ints(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not is_matrix_of_floats_ints(m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not is_rectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not is_rectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_sum = []
    for i in range(len(m_a)):
        lst_sum = []
        for j in range(len(m_b[0])):
            num_sum = 0
            for k in range(len(m_a[0])):
                num_sum += m_a[i][k] * m_b[k][j]
            lst_sum.append(num_sum)
        matrix_sum.append(lst_sum)
    return matrix_sum


def is_empty(matrix):
    """Check if matrix or one of its elements is empty."""
    if matrix == [] or matrix == [[]]:
        return 1
    for lst in matrix:
        if lst == [] or lst == [[]]:
            return 1
    return 0


def is_matrix(matrix):
    """Checks if matrix is a list of lists."""
    for lst in matrix:
        if type(lst) != list:
            return 0
    return 1


def is_matrix_of_floats_ints(matrix):
    """Checks if matrix contains only floats and integers."""
    for lst in matrix:
        for num in lst:
            if type(num) != int and type(num) != float:
                return 0
    return 1


def is_rectangle(matrix):
    """Checks if all rows are of the same size."""
    length = len(matrix[0])
    if (sum([1 for lst in matrix if len(lst) != length]) >= 1):
        return 0
    return 1
