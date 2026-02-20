def format_student_data(student):
    """
    Formats a student tuple into a string: 
    "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"
def display_students(students):
    """
    Loops through all students and prints formatted info.
    """
    for student in students:
        print(format_student_data(student))
def student_generator(students, major):
    """
    Returns a generator expression of students filtered by major.
    """
    return (student for student in students if student[2] == major)
