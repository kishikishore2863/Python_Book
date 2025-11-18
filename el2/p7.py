#Create a set of first letters of each word in a given paragraph.

str ="India is my Country"
list1 = str.split(" ")
print(list1)
set = set()
for i in list1:
    set.add(i[0])
print(set)    