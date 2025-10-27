numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of__evens = [x**2 for x in numbers if x % 2 == 0]
print (squares_of__evens)

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
flattened = [num for row in matrix for num in row]
print(flattened)

l1 = []
for x in range(5):
    l1.append("hello")

print(l1)    