ANIMALS = [
    {
      "id": 2,
      "name": "Ruby",
      "breed": "Lab",
      "customerId": 2,
      "locationId": 5
    },
    {
      "id": 3,
      "name": "Major",
      "breed": "Lab",
      "customerId": 3,
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Kia",
      "breed": "Husky",
      "customerId": 4,
      "locationId": 2
    },
    {
      "id": 5,
      "name": "Savannah",
      "breed": "Dummy",
      "customerId": 5,
      "locationId": 3
    }
  ]

def get_all_animals():
    return ANIMALS

def get_single_animal(id):

    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    
    max_id = ANIMALS[-1]["id"]
    
    new_id = max_id + 1
    
    animal["id"] = new_id
    
    ANIMALS.append(animal)
    
    return animal