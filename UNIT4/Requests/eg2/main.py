import requests
import csv



res = requests.get('https://dummyjson.com/posts')
data = res.json()
posts = data['posts']

with open('api_data.csv','w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(['id','title','body'])
    for post in posts:
        writer.writerow([post['id'],post['title'],post['body']])
print("Data saved")

