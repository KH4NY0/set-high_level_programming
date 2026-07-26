#!/usr/bin/python3
"""Defines a base geometry class with an integer validator."""


class BaseGeometry:
    """Represents the base of all geometry shapes."""

    def area(self):
        """Raise an Exception, since area is not implemented here.

        Raises:
            Exception: always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: the name of the value, used in the error messages.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
