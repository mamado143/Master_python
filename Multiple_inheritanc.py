class BaseOne:
    def __init__(self):
        print("BaseOne.")
    def fun_one(self):
        print("BaseOne fun")

class BaseTwo:
    def __init__(self):
        print("BaseTwo.")
    def fun_two(self):
        print("BaseTwo fun")

class Derived(BaseOne, BaseTwo):
    pass

My_Dr = Derived()
My_Dr.fun_one()
My_Dr.fun_two()
# print(Derived.mro())
# print(My_Dr.fun_one)
# print(My_Dr.fun_two)
