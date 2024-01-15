#!/usr/bin/python3
"""Rectangle base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class (blueprint) for rectangle object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init rectangle object.

        Args:
            width: width of the new Rectangle.
            height: height of the new Rectangle.
            x: x coordinate of the new Rectangle.
            y: y coordinate of the new Rectangle.
            id: to avoid duplicating the same code.
        Raises:
            TypeError: If the input is not an integer
            ValueError: if either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: if either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set the width of the rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set the x coordinate of the rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set the y coordinate of the rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the char #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for _y_ in range(self.y)]
        for _height_ in range(self.height):
            [print(" ", end="") for _x_ in range(self.x)]
            [print("#", end="") for _width_ in range(self.width)]
            print("")

    def __str__(self):
        """
        overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        Args:
            *args: attribute values.
                1st argument should be the id attribute.
                2nd argument should be the width attribute.
                3rd argument should be the height attribute.
                4th argument should be the x attribute.
                5th argument should be the y attribute.
        """
        arg_increment = 0
        if args and len(args) != 0:
            for _arg_ in args:
                if arg_increment == 0:
                    if _arg_ is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = _arg_
                elif arg_increment == 1:
                    self.width = _arg_
                elif arg_increment == 2:
                    self.height = _arg_
                elif arg_increment == 3:
                    self.x = _arg_
                elif arg_increment == 4:
                    self.y = _arg_

                arg_increment = arg_increment + 1

        elif kwargs and len(kwargs) != 0:
            for _key_, _val_ in kwargs.items():
                if _key_ == "id":
                    if _val_ is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = _val_
                elif _key_ == "width":
                    self.width = _val_
                elif _key_ == "height":
                    self.height = _val_
                elif _key_ == "x":
                    self.x = _val_
                elif _key_ == "y":
                    self.y = _val_

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
