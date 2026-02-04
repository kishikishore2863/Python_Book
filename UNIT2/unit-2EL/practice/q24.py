n = int(input())
s = input()
s = s.lower()
l = [0]*26
for c in s:
    l[ord(c)-97]=1
for i in l:
    if i==0:
        print("NO")
        exit(0)
print("YES")
