#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    c = len(argv)
    a = 0
    if c == 1:
        print("{}".format(a))
    else:
        for i in range(1, c):
            a = a + int(argv.__getitem__(i))
        print("{}".format(a))
