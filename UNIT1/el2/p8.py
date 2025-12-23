#Convert two lists — one of keys and one of values — into a dictionary.

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [11,22,33,44,55,66,77,88,99]
dict1 = dict()
for i in range(len(list1)):
    dict1[list1[i]] =list2[i]
print(dict1)    