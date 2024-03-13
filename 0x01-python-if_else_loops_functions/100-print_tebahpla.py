#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        a = chr(i-32)
    else:
        a = chr(i)
    print("{}".format(a), end="")
