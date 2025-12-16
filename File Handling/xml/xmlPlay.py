import xml.etree.ElementTree as xml

books = [
    {'title':'Pride and Prejudice','author':'Jane Austen','price':240,'category':'fiction'},
    {'title':'The Diary of a Young Girl','author':'Anne Frank','price':560,'category':'non-fiction'},
]

# root must be an Element, NOT ElementTree
root = xml.Element("books")

for book in books:
    book_element = xml.Element("book")
    root.append(book_element)

    book_element.set("category", book['category'])

    title = xml.SubElement(book_element, "title")
    title.text = book['title']

    author = xml.SubElement(book_element, "author")
    author.text = book['author']

    price = xml.SubElement(book_element, "price")
    price.text = str(book['price'])

# Now create ElementTree using root
tree = xml.ElementTree(root)

with open('books.xml', "wb") as f:
    tree.write(f)

print("books.xml is successfully created!")