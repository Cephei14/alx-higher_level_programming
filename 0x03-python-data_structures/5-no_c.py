#!/usr/bin/python3
def no_c(my_string):
    no_cs = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            no_cs += char
    return no_cs
