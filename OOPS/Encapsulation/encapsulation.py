class Employee:
    def __init__(self,name,salary):
        #public data members
        self.__name = name
        self.__salary = salary

    def show(self):
        print("Name: ",self.__name,"salary:",self.__salary)



emp1 = Employee("kishi",9000)
# emp1.show()
print("salary:",emp1._Employee__salary)

