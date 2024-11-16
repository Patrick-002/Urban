import sqlite3

connection = sqlite3.connect('product_base.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    connection.commit()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)', (username, email, age, 1000))

def is_included(username):
    user = cursor.execute('SELECT username FROM Users WHERE username = ?', (username,)).fetchone()
    if user is None:
        return False
    else:
        return True

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    return data

# initiate_db()
# cursor.execute('INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',(4, 'Протеин4', '5 кг', 4000))
# connection.commit()
# connection.close()