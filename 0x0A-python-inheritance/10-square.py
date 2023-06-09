#!/usr/bin/python3
"""Square Module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialize the square base on Rectangle.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
