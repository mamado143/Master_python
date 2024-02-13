#!/usr/bin/python3
import json
"""Serialize the data"""
data = {
        "name" : "khalid",
        "age" : 77,
        "married" : True,
        "courses": ["Mats", "History", "Computer Science"],
}
# convert to json formated string
json_string = json.dumps(data)

# save to a file

with open("data.json", "a") as json_file:
    json_file.write(json_string)
print(f"\n{json_string} \n")



