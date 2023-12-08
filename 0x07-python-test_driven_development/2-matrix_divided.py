#!/usr/bin/python3
"""
working on
matrix divided

"""


def matrix_divided(matrix, div):
    """
    matrix_divided take and
    return dividends
    """
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (row_size_equal(matrix) is False):
        raise TypeError("Each row of the matrix must have the same size")
    matrix_list = []
    for i in matrix:
        matrix_sub_list = []
        for j in i:
            if (type(j) is not int and type(j) is not float):
                raise TypeError("matrix must be a matrix "
                                + "(list of lists) of integers/floats")
            result = j/div
            result = round(result, 2)
            matrix_sub_list.append(result)
        matrix_list.append(matrix_sub_list)
    return matrix_list


def row_size_equal(matrix):
    """
    it check if
    matrix row are of the same size
    """
    first_length = len(matrix[0])
    all_same_lenght = all(len(row) == first_length for row in matrix[1:])
    return all_same_lenght
