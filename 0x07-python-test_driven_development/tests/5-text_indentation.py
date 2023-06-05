#!/usr/bin/python3
"""
Defines a text-indentation function.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for h in text:
        if flag == 0:
            if h == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if h == '?' or h == '.' or h == ':':
                print(h)
                print()
                flag = 0
            else:
                print(h, end="")
