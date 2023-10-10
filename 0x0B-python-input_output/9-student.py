#!/usr/bin/python3
"""module defines a class Student."""


class Student:
    """Represent a student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name (str): The 1st name of the class student.
            last_name (str): The last name of the class student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary rep of the Student."""
        return self.__dict__
