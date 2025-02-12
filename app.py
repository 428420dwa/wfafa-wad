# app.py (Flask приложение)
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = 'tickets.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    create_table() # создаем таблицу при запуске
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tickets (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()


    return render_template('index.html', )

@app.route('/add')
def about():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()
    conn.close()
    return render_template('add.html ', tickets=tickets)

if __name__ == '__main__':
    app.run(debug=True)
