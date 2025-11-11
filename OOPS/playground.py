class Student:
    school_name = "New public School";

    def __init__(self,name,clas,age):
        self.name = name
        self.clas = clas
        self.age = age

    @classmethod
    def change_name(cls,new_name):
        cls.school_name = new_name

    @staticmethod
    def info(sel):
        print("name:"+sel.name)
        print("class:"+sel.clas)
        print("age:"+sel.age)
        print("school:"+sel.school_name)



s1 = Student("kishore","9","15")
s2 = Student("halo","10","19")
# s1.info()
# s2.info()
# s1.change_name("columbia school")
s1.school_name = "pesu"
Student.info(s1)
# s2.info()
