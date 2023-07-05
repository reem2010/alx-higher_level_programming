#!/usr/bin/python3
""" in this module all elements
of a matrix will be divided by a value"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
    Args:
        matrix: the matrix
        div: the divisor
    Returns:
        return the matrix
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")
    for i in matrix:
        if (type(i) != list):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        for j in i:
            if (type(j) != int and type(j) != float):
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/float")
    size = 0
    if len(matrix) != 0:
        size = len(matrix[0])
    for j in matrix:
        if len(j) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list((map(lambda y: round(y / div, 2), new[i])))
    return (new)
