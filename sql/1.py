import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="08167482"
)

print("Connected!")
cur = conn.cursor()
#cur.execute("Insert into students (name, age) VALUES (%s, %s)",("Tami",14))
cur.execute("Select * From students")
rows=cur.fetchall()
for i in rows:
    print(i)
cur.close()
conn.close()