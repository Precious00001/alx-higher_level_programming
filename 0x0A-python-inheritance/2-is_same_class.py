#!/usr/bin/python3
"""
    Defines a class-checking function.
"""


def is_same_class(obj, a_class):
    """
    check instance and class
    Args:
        obj(object):to be checked
        a_class(anything): to be checked
    Return: Treturn true if obj is the exact class a_class, otherwise false
    """
    return type(obj) is a_class
