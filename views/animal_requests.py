import sqlite3
import json
from models import Animal

# ANIMALS = [
#     {
#       "id": 2,
#       "name": "Ruby",
#       "breed": "Lab",
#       "customerId": 2,
#       "locationId": 5,
#       "status": "Admitted"
#     },
#     {
#       "id": 3,
#       "name": "Major",
#       "breed": "Lab",
#       "customerId": 3,
#       "locationId": 1
#     },
#     {
#       "id": 4,
#       "name": "Kia",
#       "breed": "Husky",
#       "customerId": 4,
#       "locationId": 2,
#       "status": "Admitted"
#     },
#     {
#       "id": 5,
#       "name": "Savannah",
#       "breed": "Dummy",
#       "customerId": 5,
#       "locationId": 3,
#       "status": "Admitted"
#     }
#   ]

# def get_all_animals():
#     return ANIMALS

def get_all_animals():
  
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        """)

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:

            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return json.dumps(animals)

# def get_single_animal(id):

#     requested_animal = None

#     for animal in ANIMALS:
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal

def get_single_animal(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)
    
def get_animals_by_location(locationId):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, ( locationId, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def get_animals_by_status(status):

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status = ?
        """, ( status, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def create_animal(animal):
    
    max_id = ANIMALS[-1]["id"]
    
    new_id = max_id + 1
    
    animal["id"] = new_id
    
    ANIMALS.append(animal)
    
    return animal

def delete_animal(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))
        
def update_animal(id, new_animal):

    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            ANIMALS[index] = new_animal
            break