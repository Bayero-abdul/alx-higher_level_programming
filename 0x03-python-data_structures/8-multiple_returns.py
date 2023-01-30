#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        first = None
        length = 0
    else:
        first = sentence[0]
        length = len(sentence)

    return((length, first))
