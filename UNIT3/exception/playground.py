import builtins


# l =[name for name in dir(builtins)
#     if isinstance(getattr(builtins,name),type) and issubclass(getattr(builtins,name),BaseException)]
# print('errors')
# for i in l:
#     print(i)

class Coust(Exception):

    def __init__(self,salary,message="boom"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


n = int(input("enter a number"))
if not  ((n>=10) and (n<=20)):
        raise Coust(n)


