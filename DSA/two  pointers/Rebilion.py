
l=[]
n = int(input())
for i in range(n):
    l.append(input())

start =0
end = len(l)-1
count =0
while start < end and l[start] != 1:
    count +=1
    l[start] = 0

