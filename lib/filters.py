def filter_students_by_major(students, major):
    """
    Returns a list of students filtered by the given major using list comprehension.
    """
    return [student for student in students if student[2] == major]
