num = int(input())
for c in range(num):
    n,k = map(int, input().split())
    s= input()
    op =0
    i=0
    while i <len(s):
        if s[i] == 'B':
            j=1
            op += 1
            i+=k
        else:
            i+=1
    print(op)

