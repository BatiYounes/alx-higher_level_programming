#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        list = [len(sentence), None]
        new_tuple = tuple(list)
    else:
        list = [len(sentence), sentence[0]]
        new_tuple = tuple(list)
    return new_tuple
