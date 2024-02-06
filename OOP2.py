# -- OOP => Instances
class Members:
    def __init__(self, first_name, middle_name, last_name):
        self.fname = first_name
        self.age = 20
        self.mname = middle_name
        self.lname = last_name

member_one = Members("mido", "dahir", "Mohamoud")
member_two = Members("mido", "dahir", "Mohamoud")

print(member_one.fname)
print(member_two.fname)

print(member_one.age)
print(member_two.age)

print(member_one.mname)
print(member_two.mname)

print(member_one.lname)
print(member_two.lname)

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname, member_two.mname, member_two.lname)

print(member_one.__dict__)
print(member_two.__dict__)

print(Members.__dict__)

print(member_one.__class__)
print(member_two.__class__)

print(Members.__name__)