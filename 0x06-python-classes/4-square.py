#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Special method: __init__"""
    def __init__(self, size=0):
        """Private instance attribute: self.__size"""
        self.__size = size

    """Setter propr """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    """public instance  method area"""
    def area(self):
        return self.__size ** 2
