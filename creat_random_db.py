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
        result = random.randint(0, 100)

        print(name, surname, result)

        cursor.execute(f'''
            INSERT INTO scores (id, name, surname, score) VALUES ({id}, "{name}", "{surname}", {result});
        ''')
        id += 1

        print("done")

    db.commit()
    db.close()

except Exception as e:
    print("Error:", e)
