import xml.etree.ElementTree as xml

tree = xml.ElementTree(file="demo.xml")
root = tree.getroot()
data = []

for d in root.findall('d'):
    dic={}
    for a in d:
        dic[a.tag] = a.text
    data.append(dic)

print(data)