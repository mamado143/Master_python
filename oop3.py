# oop3.py
class Members:
    not_allowed_names = ["Hell", "Shit", "Wasmo"]
    users_num = 0
    
    
    @classmethod
    def show_users_count(cls):
        print(f"We have {cls.users_num} in our system.")
         
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name
        self.age = 20
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender
        Members.users_num += 1  #Members.users
    
    def full_name(self):
        if self.fname in Members.not_allowed_names:
            raise ValueError("Name Not Allowed")
        else:
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
        return f"{self.name_with_title()}\n\nYour Full Name is  {self.full_name()}\n"

    def delete_user(self):
        Members.users_num -= 1

        return f"User {self.fname} Deleted"


print("#" * 50)
print(Members.users_num)
member_one = Members("Mido", "Dahir", "Mohamoud", "Male")
member_two = Members("Hamda", "Saciid", "Mohamoud", "Female")
Member_Three = Members("siil", "Khalid", "siciid", "Male")
print(member_one.get_all_info())
print(member_two.get_all_info())
print(Members.users_num )
print(Member_Three.delete_user())
print(Members.users_num)
Members.show_users_count()
print("#" * 50)
print(Members.full_name(member_one))

