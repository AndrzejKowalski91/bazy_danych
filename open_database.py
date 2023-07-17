import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE scores(
    id integer, 
    name string, 
    surname string, 
    score integrer)

''')

db.commit()
db.close()