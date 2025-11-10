class Student:
    # Class variable (shared by all instances)
    school_name = "ABC Public School"

    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age

    # Instance method
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

    # Class method – operates on the class, not instances
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to: {cls.school_name}")

    # Static method – doesn’t depend on class or instance
    @staticmethod
    def is_adult(age):
        return age >= 18


# Example usage
s1 = Student("Kishore", 20)
s2 = Student("Rahul", 16)

s1.display()
s2.display()

# Using class method
Student.change_school("PES College")

s1.display()
s2.display()

# Using static method
print(Student.is_adult(20))  # True
print(Student.is_adult(15))  # False