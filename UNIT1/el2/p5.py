#Given two lists, find all elements that are common using set comprehension.
list1 = [1,2,2,3,4,5,6,7,8,9,0,1,2,4,5,8,0]
list2=[11,12,2,12,15,16,17,19,15,12,19,13,14,16,17,8,8]
set1 = {i for i in list1 if i in list2}
print(set1)