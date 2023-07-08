import json

# JASONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN from Element Animation
# The JSON format

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Convert to JSON format
personJSON = json.dumps(person, indent=4)
print(personJSON)
print()

# Convert dictionary to JSON and put it in a file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Convert JSON object to dictionary
person = json.loads(personJSON)
print(person)
print()

# Convert JSON file to dictionary
with open("person.json", "r") as file:
    example = json.load(file)
print(example)
print("\n")


# How to create an encoder for a custom class
# This will be our custom class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Option 1, create a method that returns a serializable object, in this case, a dictionary
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type " + o.__class__.__name__ + " is not JSON serializable")

# Option 2, a custom JSON encoder that overrides the original .default() method
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)

example_user = User("Max", 27)
userJSON = json.dumps(example_user, default=encode_user) # Option 1
userJSON = json.dumps(example_user, cls=UserEncoder) # Option 2
userJSON = UserEncoder().encode(example_user) # Option 3, possible because of Option 2's class
print(userJSON)


# Decoder for a custom class
# You can just decode into a dictionary like this:
example_user_decoded_dict = json.loads(userJSON)

# But if you want to decode back into your custom User class...
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    else:
        return dct

example_user_decoded_User = json.loads(userJSON, object_hook=decode_user)