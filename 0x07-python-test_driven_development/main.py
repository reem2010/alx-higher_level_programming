#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [[3]]
try:
    print(matrix_divided([[3, 9], [12, 15]], 0))
except Exception as e:
    print(e)
