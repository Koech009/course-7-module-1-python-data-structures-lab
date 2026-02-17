# This module contains functions to lazily generate student data.
from lib.student_data import students


def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    return (student for student in student_list if student[2].lower() == major.lower())


gen = student_generator(students, "computer science")

for student in gen:
    print(student)
