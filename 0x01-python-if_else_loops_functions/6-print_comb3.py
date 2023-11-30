#!/usr/bin/python3
for i in range(0, 9, 1):
    for j in range(i+1, 10, 1):
        if (i == 8):
            print("{:d}{:d}".format(i, j), end="\n")
            break
        if i != j:
            print("{:d}{:d}".format(i, j), end=", ")
