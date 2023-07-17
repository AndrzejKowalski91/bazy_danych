import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

insert into scores (id, name, surname, score) values (1, "Andrzej" , "Kowalski", 27)

''')

db.commit()
db.close()