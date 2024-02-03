def myDecorator(func):
    def nestedFunc(*args, **kwargs):
        print("Before calling the function")
        func(*args, **kwargs)
        print("After calling the function")

    return nestedFunc

@myDecorator
def sayHello():
    print("Hello From say Hello Function")

@myDecorator
def sayHowdy():
    print("Howdy From say Howdy Function")

@myDecorator
def calculate(n1, n2):
    print(n1 + n2)

sayHello()
sayHowdy()
calculate(10, 20)
