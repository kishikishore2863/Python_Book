#From a list containing duplicate numbers, build a set of unique numbers using comprehensions

list_of_duplicates = [1,2,1,2,4,5,6,7,2,9,4,7]
unique = {i for i in list_of_duplicates}
print(unique)

s = list(set(list_of_duplicates))
print(s)