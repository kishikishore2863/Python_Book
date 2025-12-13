a = {1:1,2:2,3:3}
# if 2 in a:
#     a[2]=200
# print(a)

for k,v in a.items():
    if k == 3:
        a[k] = 300
print(a)