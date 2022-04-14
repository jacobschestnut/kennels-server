EMPLOYEES = [
    {
      "id": 1,
      "name": "Michael Douglas the Original one",
      "locationId": "4"
    },
    {
      "id": 2,
      "name": "Michelle Obama",
      "locationId": 4
    },
    {
      "id": 3,
      "name": "James from Accounting",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Mace Windu",
      "locationId": 5
    },
    {
      "id": 5,
      "name": "Michael Douglas 2",
      "locationId": 3
    }
  ]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    
    requested_employee = None
    
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
            
    return requested_employee

def create_employee(employee):
    
    max_id = EMPLOYEES[-1]["id"]
    
    new_id = max_id + 1
    
    employee["id"] = new_id
    
    EMPLOYEES.append(employee)
    
    return employee