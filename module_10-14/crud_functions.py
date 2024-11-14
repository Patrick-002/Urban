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
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    return data

# initiate_db()
# cursor.execute('INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)',(4, 'Протеин4', '5 кг', 4000))
# connection.commit()
# connection.close()