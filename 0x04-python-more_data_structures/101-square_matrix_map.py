#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda s: list(map(lambda m: m**2, s)), matrix)))
