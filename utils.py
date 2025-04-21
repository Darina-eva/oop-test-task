def calculate_average_hw_grade(students, course):
    total_grades = []
    
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    
    if not total_grades:
        return 0
    
    return sum(total_grades) / len(total_grades)


def calculate_average_lecture_grade(lecturers, course):
    total_grades = []
    
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    
    if not total_grades:
        return 0
    
    return sum(total_grades) / len(total_grades)
