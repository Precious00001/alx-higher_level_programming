#!/usr/bin/python3

"""Module Square."""


class Square:
    """Square class defined by geometric shape."""

    def __init__(self, size=0, position=(0, 0)):
        """Create a new square and set it up.
        Args:
            size (int): Length of one side of the square..
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve/assign the present dimension of the square.."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve/assign the present dimension of the square.."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Display the square using the "#" character."""
        if self.__size == 0:
            print("")
            return

        [print("") for v in range(0, self.__position[1])]
        for v in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
