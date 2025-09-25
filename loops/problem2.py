# given a number display sum of number of n
n = int(input("enter number"))
sum = 0
for i in range(n,0,-1):
    sum = sum + i

print(sum)