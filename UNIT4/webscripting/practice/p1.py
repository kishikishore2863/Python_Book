import requests
from  bs4 import  BeautifulSoup

res1 = requests.get("https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/")
res = requests.get("https://www.reddit.com/")
res = requests.get("https://www.reddit.com/")
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.find('a'))

all_p =  soup.findAll('faceplate-screen-reader-content')
for i in all_p:
    print(i)