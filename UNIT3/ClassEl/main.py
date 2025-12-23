import csv
import xml.etree.ElementTree as xml

movies = list()
with open('Movie Assignment Data for Class.csv','r') as f:
    reader = csv.DictReader(f)
    i=0
    for row in reader:
        map1 ={}
        if i<=5:
            i +=1
            map1['director_name'] = row['director_name']
            map1['language'] = row['language']
            map1['color'] = row['color']
            map1['movie_title'] = row['movie_title']
            map1['genres'] = [g.strip() for g in row['genres'].split('|')]
            movies.append(map1)

root = xml.Element("movies")

for movie in movies:
    movie_element = xml.Element('movie')
    root.append(movie_element)
    movie_element.set("color",movie['color'])
    title = xml.SubElement(movie_element,'title')
    title.text = movie['movie_title']
    director = xml.SubElement(movie_element,'director')
    director.text = movie["director_name"]
    genres_element = xml.SubElement(movie_element, 'genres')
    for genre in movie['genres']:
        genret = xml.SubElement(genres_element, 'genre')
        genret.text = genre

tree = xml.ElementTree(root)
with open('movies.xml','wb')as fh:
    tree.write(fh)
print("movie created successfully")
