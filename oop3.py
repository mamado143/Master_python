# oop3.py
class Members:
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.age = 20
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
    
    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname} {self.gender}"
    
    def initials(self):
        return f"{self.fname[0]}.{self.mname[0]}.{self.lname[0]}."

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}!"
        elif self.gender == "Female":
            return f"Hello Miss {self.fname}!"
        else:
            return f"{self.fname}"
    
    def get_all_info(self):
        return f"{self.name_with_title()}\n, Your Full Name is  {self.full_name()}\n"
member_one = Members("Mido", "Dahir", "Mohamoud", "Male")
member_two = Members("Hamda", "Saciid", "Mohamoud", "Female")

print(member_one.get_all_info())
print(member_two.get_all_info())