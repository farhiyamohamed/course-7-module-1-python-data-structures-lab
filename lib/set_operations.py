def unique_majors(students):
    """
    Returns a set of unique student majors using set comprehension.
    """
    return {student[2] for student in students}
stds = [
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
]
print(unique_majors(stds))
# Output: {'Mathematics', 'Physics'}
