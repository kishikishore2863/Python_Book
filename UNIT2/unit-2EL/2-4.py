#A course class uses a class method to build objects with default credits.
# You must create three courses using this method and print details.

class Course:

    def __init__(self,name,credits):
        self.name = name
        self.credits = credits

    @classmethod
    def with_default_credits(cls,name,default_credits=3):
        return cls(name,default_credits)
    
    def display(self):
        print(f"Course:{self.name},Credits:{self.credits}")


c1 = Course.with_default_credits("Python Programing")
c2 = Course.with_default_credits("data Structures")
c3 = Course.with_default_credits("Operating Systems")

c1.display()
c2.display()
c3.display()


