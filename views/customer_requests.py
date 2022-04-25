import sqlite3
import json
from models import Customer

# CUSTOMERS = [
#     {
#       "id": 1,
#       "name": "The Rock",
#       "address": "976 Software School Rd.",
#       "phone": "615-200-7895",
#       "email": "syd@test.com"
#     },
#     {
#       "id": 2,
#       "name": "Robert Paulson",
#       "address": "123 NSS Ln.",
#       "phone": "450-322-3596",
#       "email": "trev@test.com"
#     },
#     {
#       "id": 3,
#       "name": "Lance Bass",
#       "address": "456 Road St.",
#       "phone": "123-428-1248",
#       "email": "lance@test.com"
#     },
#     {
#       "id": 4,
#       "name": "John",
#       "address": "456 Oops Dr.",
#       "phone": "371-529-9356",
#       "email": "john@test.com"
#     },
#     {
#       "id": 5,
#       "name": "Stance Bass",
#       "address": "123 Road St.",
#       "phone": "615-867-5309",
#       "email": "stance@test.com"
#     },
#   ]

def get_all_customers():
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.phone,
            c.email
        FROM Customer c
        """)

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'],
                            row['phone'], row['email'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.phone,
            c.email
        FROM Customer c
        WHERE c.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'],
                        data['phone'], data['email'])

        return json.dumps(customer.__dict__)
    
def get_customers_by_email(email):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def create_customer(customer):
    
    max_id = CUSTOMERS[-1]["id"]
    
    new_id = max_id + 1
    
    customer["id"] = new_id
    
    CUSTOMERS.append(customer)
    
    return customer

def delete_customer(id):
   
    customer_index = -1
    
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
         
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
        
def update_customer(id, new_customer):

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break