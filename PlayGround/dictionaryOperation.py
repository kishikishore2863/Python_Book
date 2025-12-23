dict ={"kishore":{"age":22,"section" :"b"}, "jhonny":{"age":80,"section":"c"}}
print(dict["kishore"]["age"]);


dict1 = {"name":"kishore"}
print(dict1)

students = [{"name":"kishore","scores":{"math":80},"sci":90}]

print(students)

sq ={x:x**2 for x in range(1,6)}
print(sq)

sq1 ={x:"even " for x in range(1,20) if x%2==0};
print(sq1)


list=["a","b","c","d","e"]

sq2 = {list[x]:x for x in range(1,5)}
print(sq2)





li = [1, 2, 3, 4, 5]
it = iter(li)
while(it):
     try:
        print(next(it))
     except StopIteration:
        break

