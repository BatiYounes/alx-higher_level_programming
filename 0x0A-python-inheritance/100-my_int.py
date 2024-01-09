#!/usr/bin/python3
"""class MyInt that inherits from int."""


class MyInt(int):
    """cIass invert operators == and !="""

    def __eq__(self, myInt):
        """invert == opeartor with !="""
        return self.real != myInt

    def __ne__(self, myInt):
        """invert != operator with =="""
        return self.real == myInt
