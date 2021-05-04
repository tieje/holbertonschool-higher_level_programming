#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return
    for i in range(len(matrix)):
        mat_len = len(matrix[i])
        for x in range(mat_len):
            if x < mat_len - 1:
                print("{:d}".format(matrix[i][x]), end=" ")
        if x == mat_len - 1:
            print("{:d}".format(matrix[i][x]), end="\n")
