#!/usr/bin/python3
"""Defines a class that only accepts one dynamic instance attribute."""


class LockedClass:
    """Blocks new instance attributes other than first_name."""

    __slots__ = ["first_name"]
