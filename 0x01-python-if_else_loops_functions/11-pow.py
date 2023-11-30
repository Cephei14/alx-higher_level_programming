#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b > 0:
        if a >= 0:
            for i in range(b):
                c = c*a
            return c
        if a < 0:
            for i in range(b):
                c = c * a
            return c
    elif b == 0:
        return 1
    else:
        for i in range(-b):
            c = c / a
        return c
