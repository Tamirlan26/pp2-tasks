import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="08167482"
)

print("Connected!")
cur=conn.cursor()
cur.execute("Delete From students Where name=%s",("Tami",))
conn.commit()
cur.execute("Select * From students")
r=cur.fetchall()
for i in r:
    print(i)
cur.close()
conn.close()