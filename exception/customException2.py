class SalaryNotInRangeError(Exception):

    def __init__(self,salary,message="salary is not in (5000,15000)range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = input(input("enter a salary amount:"))
if not 5000 < salary < 1500:
    raise SalaryNotInRangeError(salary)