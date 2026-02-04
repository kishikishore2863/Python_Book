import json

with open('demo.json','r')as f:
    ob = json.load(f)
    print(type(ob))