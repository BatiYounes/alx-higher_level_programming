#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        sub_matrix = map(lambda num: num**2, row)
        result.append(list(sub_matrix))
    return result
