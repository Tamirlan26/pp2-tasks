import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="08167482"
)

print("Connected!")
cur=conn.cursor()
cur.execute("Insert into students (name, age) VALUES (%s, %s)",("Tami",14))
cur.execute("Update students SET age=%s where name=%s",(17,"Ali"))
conn.commit()
cur.execute("Select * From students")
b=cur.fetchall()
for i in b:
    print(i)
cur.close()
conn.close()

