import sqlite3

try:
    conn=sqlite3.connect("college.db")
    conn.execute(
        "INERT INTO student VALUES(?,?,?,?)",
        (1,"another student",20,"cse")
    )
    conn.commit()

except  sqlite3.IntegrityError:
    print("student id already exits")

except sqlite3.Error as error:
    print("database error:",error)

finally:
    if "conn" in locals():
        conn.close()