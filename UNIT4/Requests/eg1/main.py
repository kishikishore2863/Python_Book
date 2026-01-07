
import requests
import json
response = requests.get('https://dummyjson.com/posts/1')
data = response.json()
print(data)

with open('api_json.json','w')as file:
    json.dump(data,file,indent=4)


if response.status_code == 200:
    print('Request sucessful!')
    print(response.text)
else:
    print(response.status_code)