from faker import Faker
fake = Faker()
# fake = Faker('he_IL')  using hebrew
from db import query_db
import random


def create_fake_customers():
    for i in range(40):
        sql = f""" INSERT INTO customers (customer_name, phone_number, discount)
        VALUES ('{fake.name()}','{fake.phone_number()}', '{random.randint(0, 12)}')"""
        query_db(sql)

def create_fake_orders():
    for i in range(20):
        sql = f""" INSERT INTO orders (customer_id, license_number, date, wash_type, car_type, price)
        VALUES ('{random.randint(0, 40)}','{random.randint(600000, 700000)}','{fake.date()}','{random.choice(["external", "internal", "polish"])}', '{random.choice(['private', 'truck', 'bus'])}', '{random.randint(40, 300)}')"""
        query_db(sql)


# create_fake_customers()
create_fake_orders()
