#!/usr/bin/python3
for i in range(0, 10, 1):
    for j in range(0, 10, 1):
        if i == 9 and j == 9:
            print("{:d}{:d}".format(i, j))
            break
        else:
            print("{:d}{:d}".format(i, j), end=", ")
