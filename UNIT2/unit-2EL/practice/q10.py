try:
    print(10/0)
except Exception as e:
    print(f"denominator can't be a zero {e}")

d =dict({1:"12",2:"2"})
d.clear()
print(d)

list1 = ["apple","banana","apple","orange","banana","apple"]
d={}
for i in list1:
    if i in d:
        d[i]= d.get(i)+1
    else:
        d[i]= 1

print(d)



