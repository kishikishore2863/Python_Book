#Given a list of numbers, create a dictionary with number as key and cube as value only if number is even
list1 = [1,2,3,4,5,6,7,8,9]
# dict1 = { i:(i**3) for i in list1 if i%2 == 0}
# print(dict1)

di ={i:i**3for i in list1 if i%2==0}
print(di)