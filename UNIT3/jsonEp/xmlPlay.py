"""
===========================================================
XML PACKAGE IN PYTHON — COMPLETE CODE DOCUMENTATION
===========================================================

This file demonstrates:
1. XML basics
2. xml.etree.ElementTree (MOST IMPORTANT)
3. Reading XML
4. Writing XML
5. Modifying XML
6. Searching XML
7. Attributes handling
8. Namespaces
9. Pretty printing
10. DOM (minidom)
11. SAX parsing (event-driven)
===========================================================
"""

# =========================================================
# 1. IMPORTING XML MODULES
# =========================================================

import xml.etree.ElementTree as ET
from xml.dom import minidom
import xml.sax

# =========================================================
# 2. CREATING XML FROM SCRATCH (ElementTree)
# =========================================================

root = ET.Element("students")

student1 = ET.SubElement(root, "student")
ET.SubElement(student1, "name").text = "Kishore"
ET.SubElement(student1, "roll").text = "101"
ET.SubElement(student1, "dept").text = "CSE"

student2 = ET.SubElement(root, "student")
ET.SubElement(student2, "name").text = "Arjun"
ET.SubElement(student2, "roll").text = "102"
ET.SubElement(student2, "dept").text = "ECE"

tree = ET.ElementTree(root)
tree.write("students.xml", encoding="utf-8", xml_declaration=True)

# =========================================================
# 3. READING XML FILE
# =========================================================

tree = ET.parse("students.xml")
root = tree.getroot()

print("Root tag:", root.tag)

for student in root:
    for child in student:
        print(child.tag, ":", child.text)
    print("------")

# =========================================================
# 4. ACCESSING ELEMENTS
# =========================================================

# First student
first_student = root[0]
print(first_student.find("name").text)
print(first_student.find("roll").text)

# =========================================================
# 5. FIND / FINDALL / ITER
# =========================================================

# find() → first occurrence
name = root.find("student/name")
print("First name:", name.text)

# findall() → all matches
for name in root.findall("student/name"):
    print("Student name:", name.text)

# iter() → recursive traversal
for elem in root.iter():
    print(elem.tag)

# =========================================================
# 6. ATTRIBUTES IN XML
# =========================================================

root = ET.Element("books")

book = ET.SubElement(root, "book", attrib={"id": "B101"})
ET.SubElement(book, "title").text = "Python"
ET.SubElement(book, "price").text = "500"

tree = ET.ElementTree(root)
tree.write("books.xml")

# Reading attributes
tree = ET.parse("books.xml")
root = tree.getroot()

for book in root:
    print(book.attrib["id"])
    print(book.find("title").text)

# =========================================================
# 7. MODIFYING XML
# =========================================================

tree = ET.parse("students.xml")
root = tree.getroot()

for student in root.findall("student"):
    if student.find("name").text == "Kishore":
        student.find("dept").text = "AI-ML"

tree.write("students_updated.xml")

# =========================================================
# 8. DELETING ELEMENTS
# =========================================================

tree = ET.parse("students.xml")
root = tree.getroot()

for student in root.findall("student"):
    if student.find("roll").text == "102":
        root.remove(student)

tree.write("students_deleted.xml")


# =========================================================
# 9. PRETTY PRINTING XML
# =========================================================

def prettify(elem):
    rough = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough)
    return reparsed.toprettyxml(indent="  ")


print(prettify(root))

# =========================================================
# 10. XML NAMESPACES
# =========================================================

ns = {"ns": "http://example.com/schema"}

root = ET.Element("{http://example.com/schema}students")

student = ET.SubElement(root, "{http://example.com/schema}student")
ET.SubElement(student, "{http://example.com/schema}name").text = "Kishore"

tree = ET.ElementTree(root)
tree.write("ns.xml")

# Reading namespace XML
tree = ET.parse("ns.xml")
root = tree.getroot()

for student in root.findall("ns:student", ns):
    print(student.find("ns:name", ns).text)

# =========================================================
# 11. DOM PARSING (xml.dom.minidom)
# =========================================================

doc = minidom.parse("students.xml")

students = doc.getElementsByTagName("student")

for s in students:
    name = s.getElementsByTagName("name")[0].firstChild.data
    print("DOM Name:", name)


# =========================================================
# 12. SAX PARSING (EVENT-DRIVEN)
# =========================================================

class StudentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""

    def startElement(self, tag, attrs):
        self.current = tag

    def characters(self, content):
        if self.current == "name":
            print("SAX Name:", content)

    def endElement(self, tag):
        self.current = ""


parser = xml.sax.make_parser()
parser.setContentHandler(StudentHandler())
parser.parse("students.xml")

# =========================================================
# 13. WHEN TO USE WHAT
# =========================================================
"""
ElementTree → Simple, fast, MOST USED
DOM          → Small XML, needs full memory
SAX          → Very large XML (streaming)
"""

# =========================================================
# END OF XML PACKAGE DOCUMENTATION
# =========================================================