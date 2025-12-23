import json

with open("data.json", 'r') as f:
    obj = json.load(f)

for k, v in obj.items():
    print(k, end=" -> ")
    for value in v.values():
        print(value)
