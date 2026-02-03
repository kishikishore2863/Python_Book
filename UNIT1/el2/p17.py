#Use reduce() to find the maximum number in a list without using max().
from functools import reduce
nums =[10,25,3,98,45,72]
# maximum =reduce(lambda a,b:a if a>b else b,nums)
# print(maximum)

m = reduce(lambda x,y:y if y>x else x,nums)
print(m)