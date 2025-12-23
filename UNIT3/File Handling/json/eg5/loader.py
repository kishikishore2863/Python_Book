import json

with open("dumpy.json", 'r') as r:
    obj =json.load(r)

for k,v in obj.items():
    print(f"{k}->{v}")
