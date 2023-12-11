#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        end = len(row) - 1
        for idx, num in enumerate(row):
            if end != idx:
                print(("{:d} ").format(num), end="")
            else:
                print(("{:d}").format(num), end="")
        print("")
