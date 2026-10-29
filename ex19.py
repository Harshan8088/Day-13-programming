import sqlite3

conn=sqlite3.connect("college.db")

rows=conn.execute("""
SELECT student.name,marks.python,
  marks.java,marks.dbms
FROM student
JOIN marks
ON student.id=marks.student_id
""")

for row in rows:
    print(row)

conn.close()