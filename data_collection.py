import bcrypt
import sqlite3

user_name = input("Please enter a name: ")
user_password = input("Please enter a Password: ")
age = int(input("Please enter your age: "))

hashed_password = bcrypt.hashpw(user_password.encode("utf8"), bcrypt.gensalt())

print(hashed_password)

conn = sqlite3.connect('demo.db')
print("Opened Database Connection")

conn.execute("INSERT INTO EMPLOYEES (ID, USERNAME, PASSWORD, AGE) \
    VALUES (null, ?,?,?)", (user_name, hashed_password, age));

conn.commit()

print("All records Entered")
conn.close()