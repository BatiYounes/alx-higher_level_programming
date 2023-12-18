#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0

    while elements < int(x):
        try:
            print(f"{my_list[elements]}", end="")
            elements = elements + 1
        except IndexError:
            break

    print("")
    return elements
