import json

# 1. Create a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

# Serialize the dictionary
json_string = json.dumps(person, indent=4, sort_keys=True)
print(json_string)

# Deserialize the json string
person_dict = json.loads(json_string)
print(person_dict)
print(person_dict["name"])