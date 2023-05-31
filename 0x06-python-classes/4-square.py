#!/usr/bin/python3
"""Defines class Square."""

class Square:
    """Square representation."""

    def __init__(self, size=0):
        """Initializes new square.

        Args:
            size (int): The dimensions of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve/assign the present dimension of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Provide the current area of the square."""
        return (self.__size * self.__size)
