import psycopg2


conn = psycopg2.connect(
    dbname= "mydb",
    user="kishikishore",
    password="password",
    port="5432"
)

cur = conn.cursor()
cur.execute("select * from student;")
# print(cur.fetchone())
print(cur.fetchmany(2))