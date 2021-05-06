#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def squared(x): return x**2
    new_list = []
    for i in matrix:
        new_list = new_list + [list(map(squared, i))]
    return new_list
