#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)
    a, b = 0, 0
    if len_a > 0:
        a += tuple_a[0]
    if len_b > 0:
        a += tuple_b[0]
    if len_a > 1:
        b += tuple_a[1]
    if len_b > 1:
        b += tuple_b[1]
    return (a, b)
