#!/usr/bin/python3
"""Square class definition that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class (blueprint) for square object."""

    def __init__(self, size, x=0, y=0, id=None):
        """init square object.

        Args:
            size: size of the new square object.
            x: x coordinate of the new square obj.
            y: y coordinate of the new square obj.
            id: to avoid duplicating the same object.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"
        overriding the __str__ method so that it returns
        [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """set the size of the square object."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        Args:
            *args: list of arguments - no-keyworded arguments.
                1st id attribute.
                2nd size attribute.
                3rd x attribute.
                4th y attribute.
            **kwargs: x2 pointer to a dictionary: key/value keyworded arguments
        """
        arg_increment = 0
        if args and len(args) != 0:
            for _arg_ in args:
                if arg_increment == 0:
                    if _arg_ is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = _arg_
                elif arg_increment == 1:
                    self.size = _arg_
                elif arg_increment == 2:
                    self.x = _arg_
                elif arg_increment == 3:
                    self.y = _arg_

                arg_increment = arg_increment + 1

        elif kwargs and len(kwargs) != 0:
            for _key_, _val_ in kwargs.items():
                if _key_ == "id":
                    if _val_ is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = _val_
                elif _key_ == "size":
                    self.size = _val_
                elif _key_ == "x":
                    self.x = _val_
                elif _key_ == "y":
                    self.y = _val_

    def to_dictionary(self):
        """eturns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
