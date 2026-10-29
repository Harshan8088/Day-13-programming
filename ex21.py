import sqlite3

conn=sqlite3.connect("student_system.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  course TEXT NOT NULL
)
""")
conn.commit()

def add_student():
    try:
        sid=int(input("student ID:"))
        name=input("name:")
        course=input("course:")

        conn.execute(
            "INSERT INTO students VALUES(?,?,?)",
            (sid,name,course)
        )
        conn.commit()
        print("student added")
    
    except ValueError:
        print("invalid student id")
    except sqlite3.IntegrityError:
        print("sudent Id already exists")

def view_student():
    rows=conn.execute(
        "SELECT *FROM students ORDER BY id"
    ).fetchall()

    if not rows:
        print("no record found")

    for row in rows:
        print(row)


def search_student():
    try:
        sid=int(input("search student id:"))
    except ValueError:
        print("invalid id")
        return

    row = conn.execute(
        "SELECT*FROM students WHERE ID=?",
        (sid,)
    ).fetchone()

    print(row if row else "student not found")


def delete_student():
    try:
        sid=int(input("delete student id:"))
    except ValueError:
        print("invalid id")
        return

    cursor = conn.execute(
        "DELETE FROM students WHERE id=?",
        (sid,)
    )
    conn.commit()

    if cursor.rowcount:
        print("student deleted")
    else:
        print("studemnt not found")

while True: 
    print("\n---STUDENT MANAGEMENT---") 
    print("1.AddStudent") 
    print("2.ViewStudents") 
    print("3.SearchStudent") 
    print("4.DeleteStudent") 
    print("5.Exit") 
    
    choice= input("EnterChoice:")

    if choice=="1": 
        add_student() 
    elif choice=="2": 
        view_student() 
    elif choice=="3": 
        search_student() 
    elif choice=="4": 
        delete_student() 
    elif choice=="5": 
        break 
    else: 
        print("InvalidChoice")