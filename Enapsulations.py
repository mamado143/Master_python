# class Member:
#     def __init__(self, name):
#         self.__name = name # Private.


# one = Member("mido") 
# print(one.__name)
# # one.name = "Alfarabi"
# # print(one.name)


class Member:
    def __init__(self, name):
        self.__name = name # Private.
    def say_hello(self):
        return f"Hello {self.__name}"


one = Member("mido") 
print(one.say_hello())
print(one._Member__name)
# print(one.__name)
# one.name = "Alfarabi"
# print(one.name)


