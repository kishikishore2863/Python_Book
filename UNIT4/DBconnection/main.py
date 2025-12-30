import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="kishikishore",
    password="password",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * from student;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()