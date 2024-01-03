#!/usr/bin/python3
"""Defines a text_indentation method (function)."""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    ., ? and :

    Args:
        text: the string to print.
    Raises:
        TypeError: if text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
