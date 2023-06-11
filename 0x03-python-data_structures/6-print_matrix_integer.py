#!/usr/bin/python3
Prototype: def print_matrix_integer(matrix=[[]]):
    """print matrix
    Args:
        matrix: list of lists
    """
    i = 0
    j = 0
    while i < len(matrix):
        while j < len(matrix[i]):
            print(
