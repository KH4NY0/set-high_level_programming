#!/usr/bin/python3
"""Defines an int subclass with inverted equality operators."""


class MyInt(int):
    """Represents a rebellious int: == and != are swapped."""

    def __eq__(self, other):
        """Return the result of a != comparison instead of ==."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Return the result of an == comparison instead of !=."""
        return int(self) == int(other)
