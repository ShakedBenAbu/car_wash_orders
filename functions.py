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


# name = input("Enter the customer's name: ")
# phone = input("Enter the customer's phone number: ")
# discount = float(input("Enter the customer's discount: "))



# result = add_customer(name, phone, discount)
# print(result)


def delete_customer(customer_id, filename="orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        sql_query = ("DELETE FROM customers WHERE customer_id = ?")
        cur.execute(sql_query, (customer_id,))
        conn.commit()
        return "Customer deleted"

customer_id = int(input("Enter the customer's ID to delete: "))

result = delete_customer(customer_id)
print(result)