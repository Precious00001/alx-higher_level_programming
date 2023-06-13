#!/usr/bin/python3
"""This defines a function that
assigns additional attributes to objects.
"""


def add_attribute(obj, att, value):
    """It adds a new attribute to an object
    if it is feasible or permitted.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
