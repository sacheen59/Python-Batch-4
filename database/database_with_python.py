# sqlite3 => file based database

import sqlite3

# connection to database
conn = sqlite3.connect("student_info.db")

cursor = conn.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS student_info(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            age INTEGER,
            subject VARCHAR(255),
            fee INTEGER
        )
    '''
)

conn.commit()
conn.close()


# function to insert data into table

def create_student(name, email, age, subject, fee):
    conn = sqlite3.connect("student_info.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            f'''
            INSERT INTO student_info (name, email, age, subject, fee)
            VALUES(?,?,?,?,?)
            ''',(name, email, age, subject,fee)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print("The user with this email already exists.")
    finally:
        conn.close()

while True:
    choice = input("Enter 1 to insert, 2 to read, 3 to update and 4 to delete: ")
    if choice == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        age = int(input("Enter your age: "))
        subject = input("Enter your subject: ")
        fee = int(input("Enter your fee: "))
        create_student(name=name, age=age, email=email, subject=subject, fee=fee)


