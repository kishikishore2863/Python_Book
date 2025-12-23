from collections import OrderedDict
ordered_dict = OrderedDict([("d",1),("a",1),("b",2),("c",3)])
print(ordered_dict)
# OrderedDict({'a':1,'b':2,'c':3})

# //Move the value to the end

ordered_dict.move_to_end("b")
print(ordered_dict)


for key in ordered_dict:
    print(key)

# reverse a KEYS
print("printing keys in reverse order")
for key in reversed(ordered_dict):
    print(key)