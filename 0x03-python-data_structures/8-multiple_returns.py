#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        length = len(sentence)
        c = sentence[0]
        return (length, c)
