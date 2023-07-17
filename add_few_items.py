from os import name
import sqlite3
import random

try:
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    print("DB open")

    names = ["Andrzej", "Dorota", "Michał", "Bartek", "Anka", "Asia", "Kasia", "Krzysztof", "Piotr"]
    surnames = ["Kowalski", "Ordon", "Wygladała", "Bak", "Papierniak", "Gzyra", "Krawczyk", "Drobek"]
    id = 0

    for _ in range(20):
        name = random.choice(names)
        surname = random.choice(surnames)
        result = random.randit(0, 100)

        print(name, surname, result)

        cursor.execute(f'''

insert into scores (id, name, surname, score) values(
{id}, "{name}", "{surname}", {result})

''')
        id += 1

        print("done")

        db.commit()
        db.close()

except:
    print("nope")
