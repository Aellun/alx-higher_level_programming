#!/usr/bin/python3
"""This function defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Ges a dict rep of the Student.

        If attrs is a list of str, rep only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {c: getattr(self, c) for c in attrs if hasattr(self, c)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The value pairs to replace attributes with.
        """
        for c, v in json.items():
            setattr(self, c, v)
