#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        end = 0
        for j in i:
            if end < len(i) - 1:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
            end = end + 1
        print()
