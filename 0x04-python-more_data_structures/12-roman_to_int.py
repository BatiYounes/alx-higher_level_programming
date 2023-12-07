#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    new_value = 0
    int_value = 0

    for char in roman_string:
        value = roman_dict.get(char, 0)
        if value > int_value:
            new_value = new_value + value - 2 * int_value
        else:
            new_value = new_value + value
        int_value = value

    return new_value
