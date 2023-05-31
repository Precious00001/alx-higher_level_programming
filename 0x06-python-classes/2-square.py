#!/usr/bin/python3
"""Defines class Square."""


class Square:
    """Illustrate a square."""

    def __init__(self, size=0):
        """Initializes new Square.

        Args:
            size (int): The dimensions of the new square..
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
