#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    a = 0
    for c in str:
        if a == n:
            pass
        else:
            string += c
        a += 1
    return string
