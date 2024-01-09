#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """init new Rectangle.

        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() of rectangle obj."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
