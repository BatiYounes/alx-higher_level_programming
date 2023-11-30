#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1

a = 0
res = 0
for arg in sys.argv:
    if a != 0:
        res += int(arg)
    else:
        a += 1
print("{:d}".format(res))
