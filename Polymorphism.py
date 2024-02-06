# -- Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + " says Woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says Meow!"


fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())


# for xayawan in [fido, isis]:
#     print(type(xayawan))
#     print(xayawan.speak())



def pet_speak(pet):
    print(pet.speak())


pet_speak(fido)
pet_speak(isis)

# -- Polymorphism