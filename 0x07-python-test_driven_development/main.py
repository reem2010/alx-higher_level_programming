#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided
matrix = [
[1, 2, 3],
[4, 5, 6]]

print(matrix_divided(matrix, 3))

print(matrix_divided([[3]], 3))

try:
    print(matrix_divided([[3, 9], [12, 15]], 0))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[3, 9], [12, 15, 3]], 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[3, "9"], [15, 3]], 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided([[3, 9], [15, 3]]))
except Exception as e:
    print(e)

try:
    print(matrix_divided())
except Exception as e:
    print(e)
print(matrix_divided([[3]],  float('inf')))
