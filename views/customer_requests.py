CUSTOMERS = [
    {
      "id": 1,
      "name": "The Rock",
      "address": "976 Software School Rd.",
      "phone": "615-200-7895",
      "email": "syd@test.com"
    },
    {
      "id": 2,
      "name": "Robert Paulson",
      "address": "123 NSS Ln.",
      "phone": "450-322-3596",
      "email": "trev@test.com"
    },
    {
      "id": 3,
      "name": "Lance Bass",
      "address": "456 Road St.",
      "phone": "123-428-1248",
      "email": "lance@test.com"
    },
    {
      "id": 4,
      "name": "John",
      "address": "456 Oops Dr.",
      "phone": "371-529-9356",
      "email": "john@test.com"
    },
    {
      "id": 5,
      "name": "Stance Bass",
      "address": "123 Road St.",
      "phone": "615-867-5309",
      "email": "stance@test.com"
    },
  ]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer

def create_customer(customer):
    
    max_id = CUSTOMERS[-1]["id"]
    
    new_id = max_id + 1
    
    customer["id"] = new_id
    
    CUSTOMERS.append(customer)
    
    return customer