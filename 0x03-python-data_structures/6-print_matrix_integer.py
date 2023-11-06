#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("")
    for i in matrix:
        print("\n")
        for j in i:
            if (i != -1 and j != -1):
                print("{:d}".format(j), end=' ')
            else:
                print("{:d}".format(j))
    print("\n")
