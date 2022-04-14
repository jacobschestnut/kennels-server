LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville South",
      "address": "209 Emory Dr."
    },
    {
      "id": 2,
      "name": "Nashville North",
      "address": "420 Jeremy Dr."
    },
    {
      "id": 3,
      "name": "Nashville East",
      "address": "73 Tiny St."
    },
    {
      "id": 4,
      "name": "Nashville West",
      "address": "9000 Big Way"
    },
    {
      "id": 5,
      "name": "Nashville Main",
      "address": "182 Nice Rd."
    }
  ]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    
    return requested_location

def create_location(location):
    
    max_id = LOCATIONS[-1]["id"]
    
    new_id = max_id + 1
    
    location["id"] = new_id
    
    LOCATIONS.append(location)
    
    return location