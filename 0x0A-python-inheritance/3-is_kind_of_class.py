#!/usr/bin/python3
"""
    is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    A function that determines if an object is an instance of,
    or if the object is an instance of a class derived from,
    the specified class. It returns True in such cases and False otherwise.
    """
    return isinstance(obj, a_class)
