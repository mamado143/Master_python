#/usr/bin/python3
import json

"""deserializatin the data"""

# load from the file
with open("data.json", "r") as json_file:
    json_string = json_file.read()

# convert the json formatted string to a dictionary.
data = json.loads(json_string)
print(data["name"])
print(data["age"])
print(data["courses"])