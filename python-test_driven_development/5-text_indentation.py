#!/usr/bin/python3
"""Defines a text-indentation function.

This module exposes a single function, ``text_indentation``, which prints
text with two new lines after each ``.``, ``?`` and ``:`` character.
"""


def text_indentation(text):
    """Print ``text`` with two new lines after each ``.``, ``?`` and ``:``.

    Lines are printed without leading or trailing spaces.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
