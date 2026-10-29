import sqlite3

conn=sqlite3.connect("college.db")

rows=conn.execute("""
SELECT student_id,
      python + java + dbms AS total
FROM marks
""")

for row in rows:
    print("student:",row[0],"toatl:",[1])

conn.close()