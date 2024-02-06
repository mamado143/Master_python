class Member:
    def __init__(self, name):
        self.__name = name # Private.
    def say_hello(self):
        return f"Hello {self.__name}"
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name


one = Member("mido") 
print(one.say_hello())
print(one._Member__name)
print(one.get_name())
one.set_name("cudoon")
print(one.get_name())

