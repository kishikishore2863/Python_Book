import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://en.wikipedia.org/wiki/World_population"
req = Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

page = urlopen(url)
html = page.read()
print(html)
soup = BeautifulSoup(html, "html.parser")

rows = soup.find_all("tr")

data = []
for row in rows:
    cols = row.find_all("td")
    cols = [col.get_text() for col in cols]
    data.append(cols)

df = pd.DataFrame(data)
print(df)