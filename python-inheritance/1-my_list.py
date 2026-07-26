#!/usr/bin/python3
"""Defines a list subclass that can print itself sorted."""


class MyList(list):
    """Represents a list of integers that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order, leaving the list untouched."""
        print(sorted(self))
