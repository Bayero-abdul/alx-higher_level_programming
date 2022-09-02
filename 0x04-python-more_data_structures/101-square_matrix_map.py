#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix == []:
        return (None)

    return(list(map(lambda x: square_list(x), matrix)))


def square_list(my_list=[]):
    return (list(map(lambda x: x**2, my_list)))
