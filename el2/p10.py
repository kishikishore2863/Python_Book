#Create a dictionary that maps words to their lengths from a given sentence.
str = "why common sense is not common"
list1 = str.split(" ")
dict1 = {}
for i in list1:
    dict1[i] = len(i)
print(dict1)

dict2 = { i:(len(i)) for i in list1}
print(dict2)