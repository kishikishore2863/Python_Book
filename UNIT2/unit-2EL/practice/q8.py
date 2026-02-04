class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    @staticmethod
    def greet():
        print("jfhsdkfh")

a = Person.from_string("kishore-21")
print(a.name)
b =a.from_string("s-10")
print(b.name)
b.greet()