import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"],
}


person_json = json.dumps(person, indent=4, sort_keys=True)  # here sort keys will sort the string into alphabetical order, can also use {separators=[';',' = ']}
print(person_json)  # Converts json data into python string

person = json.loads(person_json)
print(person)  # Converts json data into python dictionary


with open("Example.json", "r") as file:  # do the same as upper one, but with the help of file
    person = json.load(file)
    print(person)


with open("Person.json", "w") as file:  # dumping json data into file
    json.dump(person_json, file, indent=4)