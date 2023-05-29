import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

data = [
    ("Test1","Gest1",1),
    ("Test2","Gest2",2),
    ("Test3","Gest3",3),
    ("Test4","Gest4",4),
    ("Test5","Gest5",5),
]

query_insert = "INSERT INTO users (first_name, last_name, age) VALUES (?, ?, ?)"

cursor.executemany(query_insert, data)
connection.commit()