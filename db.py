import sqlite3

def setup(filename="orders.sqlite"):  # create tables
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS customers(customer_id INTEGER PRIMARY KEY, customer_name TEXT, phone_number TEXT, discount TEXT)")
        conn.commit()
        cur.execute("CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER, license_number TEXT, date TEXT, wash_type TEXT, car_type TEXT, price TEXT, FOREIGN KEY(customer_id) REFERENCES customers(customer_id))") 
        conn.commit()


def query_db(sql, filename="orders.sqlite"):  # sql queries and return
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit
        return cur.fetchall()

orders=query_db("select * from orders")

