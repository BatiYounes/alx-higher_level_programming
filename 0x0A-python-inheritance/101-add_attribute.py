#!/usr/bin/python3
"""function that adds attributes to objects if possible"""


def add_attribute(obj, att, value):
    """add new attribute to an object if possible.

    Args:
        obj: object to add an attribute to.
        att: name of the attribute to add to object.
        value: value of attribute.
    Raises:
        TypeError: if the object can’t have new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
