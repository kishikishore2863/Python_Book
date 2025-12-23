import json

# loads()   string -> python obj(dict)
json_string = '{"name":"kishore","age":22}'
data = json.loads(json_string)

print(data)
print(type(data))

# 2. json.dumps() → Python Object ➝ JSON String

data = {
    "name":"kishore",
    "age":22,
    "language":["c","c++","java"]
}

json_str = json.dumps(data,)
print(json_str)
print(type(json_str))


#3. json.dump() → Python Object ➝ JSON File

with open("jsonData.json", 'w') as f:
    json.dump(data,f,indent=2)
print("Saved to file")

