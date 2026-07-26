#!/usr/bin/python3
"""Defines a base class for geometry shapes with an abstract area."""


class BaseGeometry:
    """Represents the base of all geometry shapes."""

    def area(self):
        """Raise an Exception, since area is not implemented here.

        Raises:
            Exception: always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")
