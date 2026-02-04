import json

# JSON string (must be enclosed in triple quotes or use proper escaping)
dic = """[
    {"name": "kishore", "stream": "science", "marks": 95},
    {"name": "harry", "stream": "science", "marks": 95},
    {"name": "kane", "stream": "science", "marks": 95}
]"""

# Convert JSON string to Python object
py_ob = json.loads(dic)

# Write Python object to a JSON file
with open('demo.json', 'w') as f:
    json.dump(py_ob, f, indent=4)

print("Data written to text.json successfully")

