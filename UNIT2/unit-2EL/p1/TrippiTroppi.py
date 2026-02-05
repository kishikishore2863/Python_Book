n = int(input())
for i in range(n):
    l = input().split()
    s=""
    for c in l:
        s +=c[0]
    print(s)