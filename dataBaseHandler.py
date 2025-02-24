import sqlite3

class DataBaseHandler:
    DB_Name = 'students.db'

    @staticmethod
    def _connect():
        return sqlite3.connect(DataBaseHandler.DB_Name)

    @staticmethod
    def create_table():
        try:
            with DataBaseHandler._connect() as conn:
                conn.execute('''CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        gender TEXT NOT NULL)''')
        except sqlite3.Error as e:
            print(f'Error while creating table! {e}')

    @staticmethod
    def insert_student(name, email, age, gender):
        try:
            with DataBaseHandler._connect() as conn:
                conn.execute('''INSERT INTO students (name, email, age, gender) VALUES (?, ?, ?, ?)''', 
                             (name, email, age, gender))
        except sqlite3.Error as e:
            print(f'Error while creating student record! {e}')

    @staticmethod
    def get_all_students():
        try:
            with DataBaseHandler._connect() as conn:
                return conn.execute('''SELECT * FROM students''').fetchall()
        except sqlite3.Error as e:
            print(f'Error while getting students records! {e}')
            return []


DataBaseHandler.create_table()