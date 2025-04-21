from constants import MAX_LECTURER_GRADE, MIN_LECTURER_GRADE


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_course(self, course):
        if course in self.courses_in_progress:
            raise ValueError(f'The student already attends {course}')
        
        self.courses_in_progress.append(course)
    
    def finish_course(self, course):
        if course not in self.courses_in_progress:
            raise ValueError(f'The student does not attend {course}')
        
        index_to_remove = self.courses_in_progress.index(course)
        finished_course = self.courses_in_progress.pop(index_to_remove)
        self.finished_courses.append(finished_course)
    
    def rate_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            raise ValueError(f'Given object is not an instance of class Lecturer')
        if course not in lecturer.courses_attached:
            raise ValueError(f'Lecturer does not belong to {course}')
        if course not in self.courses_in_progress and course not in self.finished_courses:
            raise ValueError('This student has never attended provided course, therefore you cannot rate a lecturer')
        if grade < MIN_LECTURER_GRADE or grade > MAX_LECTURER_GRADE:
            raise ValueError(f'Grade should be from {MIN_LECTURER_GRADE} to {MAX_LECTURER_GRADE}. Given grade: {grade}')
        
        if course in lecturer.grades:
            lecturer.grades[course] += [grade]
        else:
            lecturer.grades[course] = [grade]
    
    def get_average_grade(self):
        total_grades = []
    
        for _, grades in self.grades.items():
            total_grades.extend(grades)
    
        return round(sum(total_grades) / len(total_grades), 2)
    
    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\n" +\
               f"Фамилия: {self.surname}\n" +\
               f"Средняя оценка за домашние задания: {average_grade}\n" +\
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" +\
               f"Завершенные курсы: {', '.join(self.finished_courses)}"
    
    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\n" +\
               f"Фамилия: {self.surname}\n" +\
               f"Средняя оценка за лекции: {average_grade}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade == other_grade
    
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade < other_grade
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade > other_grade

    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def attach_to_course(self, course):
        if course in self.courses_attached:
            raise ValueError(f'{self} is already in this course')

        self.courses_attached.append(course)
    
    def remove_from_course(self, course):
        if course not in self.courses_attached:
            raise ValueError(f'This mentor does not belong to {course}')
        
        index_to_remove = self.courses_attached.index(course)
        del self.courses_attached[index_to_remove]


class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)
    
    def get_average_grade(self):
        total_grades = []
    
        for _, grades in self.grades.items():
            total_grades.extend(grades)
    
        return round(sum(total_grades) / len(total_grades), 2)

    def __str__(self):
        average_grade = self.get_average_grade()
        return f"Имя: {self.name}\n" +\
               f"Фамилия: {self.surname}\n" +\
               f"Средняя оценка за лекции: {average_grade}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade == other_grade
    
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade < other_grade
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented

        average_grade = self.get_average_grade()
        other_grade = other.get_average_grade()
        return average_grade > other_grade

    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other


class Reviewer(Mentor):
    
    def rate_homework(self, student, course, grade):
        if not isinstance(student, Student):
            raise ValueError(f'Given object is not an instance of class Student')
        if course not in self.courses_attached:
            raise ValueError(f'Reviewer does not belong to {course}')
        if course not in student.courses_in_progress:
            raise ValueError(f'Student does not attend {course}')

        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
