class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = []  # List of Subject objects

    def add_subject(self, subject):
        self.subjects.append(subject)

class Subject:
    def __init__(self, subject_name, teacher):
        self.subject_name = subject_name
        self.teacher = teacher
        self.grades = {}  # key: Student, value: Grade

    def add_grade(self, student, grade):
        self.grades[student] = grade

class Grade:
    def __init__(self, grade_value):
        self.grade_value = grade_value

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class ReportCard:
    def __init__(self, student):
        self.student = student
        self.subjects_grades = {}

    def generate_report(self):
        for subject in self.student.subjects:
            self.subjects_grades[subject.subject_name] = subject.grades.get(self.student, None)
        return self.subjects_grades
