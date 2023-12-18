#!/usr/bin/python3

def safe_print_list(my_list=[],x=0):
    element = 0

    while element < int(x):
        try:
            print(f"{my_lis[element]}",end="")
            element = element + 1
        except IndexError:
            break
    print("")
    return element
