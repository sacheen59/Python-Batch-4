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

def read_students():
    conn = sqlite3.connect("student_info.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * from student_info")
    rows = cursor.fetchall()
    for data in rows:
        print(
            f'''
            Name: {data[1]} | Email: {data[2]} | Age: {data[3]} | Course: {data[4]} | Fees: {data[5]}
            '''
        )
    conn.close()

def update_student(student_id, field, new_value):
    conn = sqlite3.connect("student_info.db")
    cursor = conn.cursor()
    cursor.execute(
        f'''
            UPDATE student_info
            SET {field} = ?
            WHERE id = ?
        ''', (new_value, student_id)
    )
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("student_info.db")
    cursor = conn.cursor()
    cursor.execute(
        f"DELETE FROM student_info WHERE id = ?",(student_id)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully")
    else:
        print("Student with that id doesnot exists")
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

    elif choice == "2":
        read_students()

    elif choice == "3":
        update_choice = input("Enter 1 for name, 2 for email, 3 for age, 4 for subject, 5 for fee: ")
        student_id  = input("Enter student id: ")
        if update_choice == "1":
            new_name = input("Enter the new name: ")
            update_student(student_id, "name", new_name )
        elif update_choice == "2":
            new_email = input("Enter your new email: ")
            update_student(student_id, "email", new_email)
        elif update_choice == "3":
            new_age = int(input("Enter your new email: "))
            update_student(student_id, "age", new_age)

        elif update_choice == "4":
            new_subject = input("Enter your new subject: ")
            update_student(student_id, "subject", new_subject)
        elif update_choice == "5":
            new_fee = int(input("Enter your new fee: "))
            update_student(student_id, "fee", new_fee)
        else:
            print("Invalid choice")

    elif choice == "4":
        student_id = input("Enter the id of the user: ")
        delete_student(student_id)

    else:
        print("Invalid choice")
