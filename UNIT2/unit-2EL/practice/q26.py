class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


class Player(Person):

    def __del__(self,name,age,role,statics):
        super().__init__(name,age)
        self.role = role
        self.statics = statics

class Coach(Person):

    def __init__(self,name,age,specialization,experiance):
        super.__init__(name,age)
        self.specialization =specialization
        self.experiance=experiance


class Team:
    listPlayer =[]
    coach  = 