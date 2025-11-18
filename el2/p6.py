#Given a list of numbers, create a set of numbers divisible by both 2 and 3.
list1 = [1,2,3,4,5,6,7,8,9]
set1 = {i for i in list1 if i%2 ==0 and i%3 ==0}
print(set1)