import xml.etree.ElementTree as xml

tree = xml.parse('../books.xml')
root = tree.getroot()

books = []

for book in root.findall('book'):
    book_data = {}
    book_data['category'] = book.get('category')

    for data in book:
        book_data[data.tag] = data.text

    books.append(book_data)

print(books)

for price_element in root.iter("price"):
    price = int(price_element.text)
    price = price+10
    