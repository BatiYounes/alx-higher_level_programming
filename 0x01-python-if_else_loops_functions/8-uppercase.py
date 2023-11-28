#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            upper += chr(ord(c)-32)
        else:
            upper += c
    print("{}".format(upper))
