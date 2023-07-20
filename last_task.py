import sqlite3

def create_table():
    try:
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                score INTEGER
            )
        ''')
        db.commit()
        db.close()
        print("Table created successfully!")
    except Exception as e:
        print("Error:", e)

def insert_data(name, surname, score):
    try:
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        cursor.execute(f'''
            INSERT INTO scores (name, surname, score) VALUES ("{name}", "{surname}", {score})
        ''')
        db.commit()
        db.close()
        print("Data inserted successfully!")
    except Exception as e:
        print("Error:", e)

def select_data():
    try:
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM scores")
        rows = cursor.fetchall()
        db.close()

        print("ID | Name | Surname | Score")
        print("---------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    except Exception as e:
        print("Error:", e)

def delete_data(id):
    try:
        db = sqlite3.connect("simple.db")
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM scores WHERE id={id}")
        db.commit()
        db.close()
        print("Data deleted successfully!")
    except Exception as e:
        print("Error:", e)

# Create the table if it doesn't exist
create_table()

# Insert data
insert_data("John", "Doe", 85)
insert_data("Jane", "Smith", 92)

# Print the data
print("\nData in the database:")
select_data()

# Delete data with ID=1
delete_data(1)

# Print the data after deletion
print("\nData after deletion:")
select_data()
