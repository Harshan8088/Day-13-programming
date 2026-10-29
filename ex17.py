# student marks table

import sqlite3

conn=sqlite3.connect("college.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS marks(
    student_id INTEGER PRIMARY KEY,
    python INTEGER,
    java INTEGER,
    dbms INTEGER
)
""")

conn.execute(
    "INSERT OR REPLACE INTO marks VALUES (?,?,?,?)",
    (1,85,90,80)
)

conn.commit()
conn.close()
print("marks saved")