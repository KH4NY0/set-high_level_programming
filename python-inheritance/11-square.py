#!/usr/bin/python3
"""Defines a Square class with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of each side, a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description: [Square] <size>/<size>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
