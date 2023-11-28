#!/usr/bin/python3
for numbers in range(0, 10):
    for _numbers in range(numbers + 1, 10):
        if numbers == 8 and _numbers == 9:
            print("{}{}".format(numbers, _numbers))
        else:
            print("{}{}".format(numbers, _numbers), end=", ")
