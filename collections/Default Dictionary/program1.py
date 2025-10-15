from collections import defaultdict

def def_values():
    return 'Not Existing'


d2 =defaultdict(def_values)
d2['a'] = 1
d2['b'] = 1
print(d2['a'],d2['b'],d2['c'])
print(type(d2))
print(d2)