#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

string = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    string += 's.'
elif argc == 1:
    string += ':'
else:
    string += 's:'
print(string.format(argc))

a = 0
for arg in sys.argv:
    if a != 0:
        print("{:d}: {:s}".format(a, arg))
    a += 1
