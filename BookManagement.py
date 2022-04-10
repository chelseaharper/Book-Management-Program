#Back End for Book inventory program
import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title text,
        author text,
        year integer,
        isbn integer,
        ord_quantity,
        av_quantity integer,
        dam_quantity integer,
        don_quantity integer,
        price integer,
        prod_cost integer)""")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn, ord_quantity, av_quantity, dam_quantity, don_quantity, price, prod_cost):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", (title, author, year, isbn, ord_quantity, av_quantity, dam_quantity, don_quantity, price, prod_cost))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.close()
    print(rows)
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn, ord_quantity, av_quantity, dam_quantity, don_quantity, price, prod_cost):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
    UPDATE book SET
    title=?,
    author=?,
    year=?,
    isbn=?,
    ord_quantity=?,
    av_quantity=?,
    dam_quantity=?,
    don_quantity=?,
    price=?,
    prod_cost=?
    WHERE id=?""",
    (
        title,
        author,
        year,
        isbn,
        ord_quantity,
        av_quantity,
        dam_quantity,
        don_quantity,
        price,
        prod_cost,
        id))
    conn.commit()
    conn.close()

connect()
#update(2, title="Fall of the Kumiho", author="Chelsea Harper")
#print(view())