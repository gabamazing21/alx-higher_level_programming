#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in matrix:
            for index, j in enumerate(i):
                if (index == 2):
                    print("{:d}".format(j))
                else:
                    print("{:d}".format(j), end=" ")
