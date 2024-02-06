# ---     python3 Ozero   -----
# --- OOP Training Syntax -----
#---- Magic method __init__() -
class Member:
    def __init__(self):  # constructor
        print("A new member is created")


Member()
Member()
Member()
print("-" * 40)
Member_one = Member()
Member_two = Member()
Member_three = Member()

print(Member_one.__class__)

