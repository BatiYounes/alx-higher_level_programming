#!/usr/bin/python3
def no_c(my_string):
    chars_list = ''.join([char for char in my_string if char not in 'cC'])
    return chars_list
