# update product sto k

import sqlite3

conn=sqlite3.connect("shop.db")

cursor=conn.execute(
    "UPDATE products SET stock = stock - ? "
    "WHERE ID = ? AND stock >= ?",
    (2,1,2)
)

conn.commit()

if cursor.rowcount:
    print("stock updated")
else:
    print("product missing or insufficient stock")

conn.close()