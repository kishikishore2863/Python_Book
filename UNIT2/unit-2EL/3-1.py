#A Student class stores a common university name as a class variable.
# Each student has a name and marks. A class method updates the university name for all students.
# A static method checks if a mark is valid.
# Create objects and show the updated university name across them.
class Student:
    university = "ABC University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def update_university(cls, new_name):
        cls.university = new_name

    @staticmethod
    def is_valid_mark(m):
        return 0 <= m <= 100

s1 = Student("Kishore", 85)
s2 = Student("Amit", 92)
s3 = Student("Rita", 73)

Student.update_university("National Institute of Technology")

print(s1.name, s1.marks, Student.university, Student.is_valid_mark(s1.marks))
print(s2.name, s2.marks, Student.university, Student.is_valid_mark(s2.marks))
print(s3.name, s3.marks, Student.university, Student.is_valid_mark(s3.marks))