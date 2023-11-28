#!/usr/bin/python3
for characters in range(97, 123):
    if chr(characters) != 'e' and chr(characters) != 'q':
        print("{}".format(chr(characters)), end="")
