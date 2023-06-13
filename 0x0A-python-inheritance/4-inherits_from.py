#!/usr/bin/python3
"""
    inherits_from
"""


def inherits_from(obj, a_class):
    """
    This function returns:
    True if the object is an instance of a class that directly
    or indirectly inherits from the specified class;
    otherwise, it returns False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
