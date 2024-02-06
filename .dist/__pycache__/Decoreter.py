class member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello, my name is " + self.name)
    @property 
    def age_in_days(self):
        print(self.age * 365)

one = member("mido", 36)
print(one.age)
print(one.name)
one.say_hello()
print(one.age_in_days)
