#!/usr/bin/python3
"""Defines a Student class with serialization and deserialization."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        Args:
            attrs (list): If a list of strings, only the attributes whose
                names appear in it are retrieved. Otherwise every attribute
                is retrieved.

        Returns:
            dict: The filtered dictionary representation of the Student.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace every attribute of the Student from a dictionary.

        Args:
            json (dict): A dictionary whose keys are public attribute names
                and whose values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
