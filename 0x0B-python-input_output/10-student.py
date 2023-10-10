#!/usr/bin/python3
"""function that defines Student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The first name of the class student.
            last_name (str): The last name of the class student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dict rep of the Student.

        If attrs is a list of str, represents only those attributes
        included in the list.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {c: getattr(self, c) for c in attrs if hasattr(self, c)}
        return self.__dict__
