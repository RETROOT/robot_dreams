import sqlite3

connection = sqlite3.connect("db.sqlite")
cursor = connection.cursor()

query = ("CREATE TABLE IF NOT EXISTS users ("
         "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "
         "first_name TEXT NOT NULL UNIQUE, "
         "last_name TEXT NOT NULL UNIQUE, "
         "age INTEGER NOT NULL)"
        )

cursor.execute(query)
