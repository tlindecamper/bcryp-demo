import sqlite3

conn = sqlite3.connect('demo.db')
print('Opened Database Connection')

conn.execute("DELETE FROM EMPLOYEES where ID = 2 ")
conn.commit()

print("DATA DELETE a Success")

conn.close()

