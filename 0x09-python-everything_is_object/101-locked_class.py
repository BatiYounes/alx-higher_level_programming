#!/usr/bin/python3
"""locked class."""


class LockedClass:
    """prevent the user from instantiating new instance attributes
    except if the new instance attribute is called first_name.
    """

    __slots__ = ["first_name"]
