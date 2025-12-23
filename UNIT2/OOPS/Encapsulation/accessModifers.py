class Employee:
    def __init__(self,name,project,salary): #private method
        self.name = name#public variable
        self._project = project #protected variable
        self.__salary = salary#private variable



