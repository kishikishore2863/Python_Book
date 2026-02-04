import xml.etree.ElementTree as xml

root = xml.Element("data")
data = [
    {"name":"kishore","stream":"science","marks":95},
    {"name":"harry","stream":"science","marks":95},
    {"name":"kane","stream":"science","marks":95}
]
for d in data:
    d_element =xml.Element("d")
    root.append(d_element)
    name = xml.SubElement(d_element,"name")
    name.text = d['name']
    stream = xml.SubElement(d_element,"stream")
    stream.text = d["stream"]
    marks = xml.SubElement(d_element,"marks")
    marks.text = str(d["marks"])
tree =xml.ElementTree(root)
with open('demo.xml','wb')as f:
    tree.write(f)