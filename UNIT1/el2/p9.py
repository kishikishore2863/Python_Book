#Generate a dictionary where keys are numbers from 1 to 10 and values are even/odd labels.
dict1 = dict()
for i in range(1,11):
    if i%2 == 0:
        dict1[i] = "even"
    else:
        dict1[i] = "odd"
print(dict1)

