#!/usr/bin/python3
"""
nothing outside the module
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    Args:
        matrix (lists of lists of int)
        div (int)
    Returns:
        new matrix
    """
    new_matrix = []
    if matrix is None or div is None:
        raise TypeError("div must be a number")
    # tests for div
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    # tests if the rows have the same length
    if all([len(i) == len(matrix[0]) for i in matrix]) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if div == float('inf'):
        def Zeros(x): return 0
        for i in matrix:
            new_matrix.append(list(map(Zeros, i)))
        return new_matrix

    def DivF(x):
        if type(x) != int and type(x) != float:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        result = x / div
        return round(result, 2)
    for i in matrix:
        new_matrix.append(list(map(DivF, i)))
    return new_matrix
