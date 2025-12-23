import json

name_dict = {
    'name':'kishikihsore',
    'languages':["c","c++","java","python"],
    'age':23
}

with open("dumpy.json", 'w') as file:
    json.dump(name_dict,file,indent=2)

    