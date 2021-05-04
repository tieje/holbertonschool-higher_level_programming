#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix)):
            mat_len = len(matrix[i])
            for x in range(mat_len):
                if x == mat_len - 1:
                    print("{}".format(matrix[i][x]), end="\n")
                if x < mat_len - 1:
                    print("{}".format(matrix[i][x]), end=" ")
    else:
        print("")
