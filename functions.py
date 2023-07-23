import sqlite3
from db import query_db

def load(filename = "orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        # cur.execute("SELECT * FROM orders")
        return cur.fetchall()


def add_customer(name, phone, discount,filename = "orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        sql_query = ("INSERT INTO customers (customer_name, phone_number, discount) VALUES (?, ?, ?)")
        contact_data = (name, phone, discount)
        cur.execute(sql_query, contact_data)
        conn.commit()
        return "Customer added"


name = input("Enter the customer's name: ")
phone = input("Enter the customer's phone number: ")
discount = float(input("Enter the customer's discount: "))



result = add_customer(name, phone, discount)
print(result)