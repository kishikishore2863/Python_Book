#Merge two dictionaries and keep the maximum value for each common key using comprehension.
d1 = {"a":10,"b":5,"c":8}
d2 = {"b":12, "c":3,"d":15}

# merge = {key:max(d1.get(key,0),d2.get(key,0))for key in set(d1) | set(d2)}

# print(merge)

