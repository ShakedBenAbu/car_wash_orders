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

# customer_id = int(input("Enter the customer's ID to delete: "))

# result = delete_customer(customer_id)
# print(result)

# def update_customer():
    # ??

def show_customers(filename="orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        return cur.fetchall()
    

def find_customer(customer_name, filename="orders.sqlite"):
        with sqlite3.connect(filename) as conn:
            cur = conn.cursor()
            sql_query = ("SELECT * FROM orders WHERE customer_name = ?")
            cur.execute(sql_query, customer_name)
            customer_data = cur.fetchone()
            if customer_data:
                customer_id, phone_number, discount = customer_data  
                return f"Customer found: ID={customer_id}, Name={customer_name}, Phone={phone_number}, Discount={discount}"
            else:
                return "Customer didnt found"
 
def insert_order(customer_id, license_number, date, wash_type, car_type, price, filename="orders.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        sql_query = '''
            INSERT INTO orders (customer_id, license_number, date, wash_type, car_type, price)
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        order_data = (customer_id, license_number, date, wash_type, car_type, price)
        cur.execute(sql_query, order_data)
        conn.commit()
        return "Order added"

# customer_id = int(input("Enter the customer's ID: "))
# license_number = input("Enter the license number: ")
# date = input("Enter the order date: ")
# wash_type = input("Enter the wash type: ")
# car_type = input("Enter the car type: ")
# price = input("Enter the price: ")

# result = insert_order(customer_id, license_number, date, wash_type, car_type, price)
# print(result)
