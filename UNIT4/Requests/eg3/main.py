import requests
import xml.etree.ElementTree as ET



res = requests.get('https://dummyjson.com/posts')
data = res.json()

root = ET.Element('posts')

for item in data['posts']:
    post_el = ET.SubElement(root,'post')
    id_el = ET.SubElement(post_el,'id')
    id_el.text = str(item['id'])
    title_el = ET.SubElement(post_el,'title')
    title_el.text = item['title']
    body_el = ET.SubElement(post_el,'body')
    body_el.text = item['body']
    tree = ET.ElementTree(root)
tree.write("api_data.xml",encoding='utf-8',xml_declaration=True)

print("Data saved")