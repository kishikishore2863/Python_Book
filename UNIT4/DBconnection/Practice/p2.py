import requests
from bs4 import BeautifulSoup

url = "https://www.pesuacademy.com/Academy/s/studentProfilePESUAdmin?menuId=651&url=studentProfilePESUAdmin&controllerMode=6401&actionType=5&id=0&selectedData=0"
ur1= "https://www.pesuacademy.com/Academy/s/studentProfilePESU"
url_python='https://www.pesuacademy.com/Academy/s/studentProfilePESUAdmin?controllerMode=6403&actionType=42&id=21280&menuId=653&_=1769248275361'
url_slide ='https://www.pesuacademy.com/Academy/s/studentProfilePESUAdmin?url=studentProfilePESUAdmin&controllerMode=6403&actionType=60&selectedData=21280&id=2&unitid=7fc52d14-8eae-475f-82fb-38f778bb124e&menuId=653&_=1769248275365'
url_dataStru = 'https://www.pesuacademy.com/Academy/s/studentProfilePESUAdmin?controllerMode=6403&actionType=42&id=21281&menuId=653&_=1769248275368'
cookies = {
    "JSESSIONID": "KMxi3GMYEaD2FQE7p0T_-XMGLrbFPCvLZ2Ix0QkE.ip-172-21-1-62",
    "AWSALB": "5pCcHBDfPIfX+Sjb8Oq0ds7VsJ3JdcbV0+NSFsAo9CAKi97TaFOtd+dRFn6ATfGawJuLAyUGFTQge2SAQriZgMqwbmsxbnv3ZcFl7izB6XO9dhCzwBgxflMNySmv",
    "AWSALBCORS": "5pCcHBDfPIfX+Sjb8Oq0ds7VsJ3JdcbV0+NSFsAo9CAKi97TaFOtd+dRFn6ATfGawJuLAyUGFTQge2SAQriZgMqwbmsxbnv3ZcFl7izB6XO9dhCzwBgxflMNySmv"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.pesuacademy.com/Academy/s/studentProfilePESU",
    "x-csrf-token": "cbdf61aa-6d83-402c-9581-d01da4f8f111",
    "x-requested-with": "XMLHttpRequest"
}

response = requests.get(url_dataStru, cookies=cookies, headers=headers)

print(response.status_code)
print(response.text)  # preview HTML

soup = BeautifulSoup(response.text,"html.parser")
p_all =soup.findAll("tr")
for i in p_all:
    print(i)
