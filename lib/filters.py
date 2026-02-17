# This module contains functions for filtering student data.
from lib.student_data import students


def filter_students_by_major(student_list, major):
    """
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
    return [
        student
        for student in student_list
        if student[2].lower() == major.lower()
    ]


result = filter_students_by_major(students, "computer science")

for student in result:
    print(student)
