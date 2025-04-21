from courses import Student, Lecturer, Reviewer
from utils import calculate_average_hw_grade, calculate_average_lecture_grade


def main():
    student1 = Student('Иван', 'Иванов', 'мужской')
    student2 = Student('Мария', 'Петрова', 'женский')
    
    reviewer1 = Reviewer('Алексей', 'Сидоров')
    reviewer2 = Reviewer('Елена', 'Козлова')
    
    lecturer1 = Lecturer('Петр', 'Смирнов')
    lecturer2 = Lecturer('Ольга', 'Васильева')
    
    student1.add_course('Python')
    student1.add_course('Git')
    student2.add_course('Python')
    student2.add_course('SQL')
    
    lecturer1.attach_to_course('Python')
    lecturer1.attach_to_course('Git')
    lecturer2.attach_to_course('Python')
    lecturer2.attach_to_course('SQL')
    
    reviewer1.attach_to_course('Python')
    reviewer1.attach_to_course('Git')
    reviewer2.attach_to_course('Python')
    reviewer2.attach_to_course('SQL')
    
    reviewer1.rate_homework(student1, 'Python', 9)
    reviewer1.rate_homework(student1, 'Python', 10)
    reviewer1.rate_homework(student1, 'Git', 8)
    reviewer2.rate_homework(student2, 'Python', 7)
    reviewer2.rate_homework(student2, 'Python', 8)
    reviewer2.rate_homework(student2, 'SQL', 9)
    
    student1.rate_lecturer(lecturer1, 'Python', 9)
    student1.rate_lecturer(lecturer1, 'Git', 10)
    student1.rate_lecturer(lecturer2, 'Python', 8)
    student2.rate_lecturer(lecturer1, 'Python', 7)
    student2.rate_lecturer(lecturer2, 'Python', 9)
    student2.rate_lecturer(lecturer2, 'SQL', 10)
    
    student1.finish_course('Git')
    student2.finish_course('SQL')
    
    print("=== Информация о студентах ===")
    print(student1)
    print()
    print(student2)
    print()
    
    print("=== Информация о рецензентах ===")
    print(reviewer1)
    print()
    print(reviewer2)
    print()
    
    print("=== Информация о лекторах ===")
    print(lecturer1)
    print()
    print(lecturer2)
    print()
    
    print("=== Сравнение лекторов ===")
    print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
    print(f"lecturer1 != lecturer2: {lecturer1 != lecturer2}")
    print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
    print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
    print(f"lecturer1 <= lecturer2: {lecturer1 <= lecturer2}")
    print(f"lecturer1 >= lecturer2: {lecturer1 >= lecturer2}")
    print()

    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]
    
    python_hw_avg = calculate_average_hw_grade(students_list, 'Python')
    python_lecture_avg = calculate_average_lecture_grade(lecturers_list, 'Python')
    
    print("=== Средние оценки по курсам ===")
    print(f"Средняя оценка за домашние задания по курсу Python: {python_hw_avg:.2f}")
    print(f"Средняя оценка за лекции по курсу Python: {python_lecture_avg:.2f}")


if __name__ == '__main__':
    main()
