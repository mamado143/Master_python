#!/usr/bin/python3

from uuid import uuid1, uuid4

# Generate a UUID based on the host ID, current time and a random number

my_uuid = uuid1()   

your_uuid = str(uuid1())

# Generate a UUID1

my_uuid =   uuid4()

# Print them out

print(my_uuid)
print(your_uuid)
