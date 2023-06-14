#!/usr/bin/python3
"""
Defines a file-writing function.
"""


def write_file(filename="", text=""):
    """
    The function returns the count of characters
    that were written from the "text" to the "filename".
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
