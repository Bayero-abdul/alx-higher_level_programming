#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        new_list = [[num**2 for num in row] for row in matrix]
        return (new_list)
