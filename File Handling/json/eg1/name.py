import json

with open("name.json", 'r') as file:
    jsonData = json.load(file)

print("type of json object:",type(jsonData))

for name in jsonData:
    print("Nmae",name)
    print("Phone Number :",jsonData[name]["number"])
    print("Age: ",jsonData[name]["age"])

    print("Address:")
    for  value in jsonData[name]["address"].values():
        print(f" {value}",end="")
    print()