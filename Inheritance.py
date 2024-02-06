class Food:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f"{self.name} is from main class and it's color is {self.color}")
    def eat(self):
        print("eat from main class")

class Apple(Food):
    def __init__(self, name, color):
        super().__init__(name, color)
        print(f"{self.name} is from sub class and it's color is {self.color}")
    
    def get_from_Tree(self):
        print("get From sub class")
    def eat(self):
        print("eat from sub class")

food_one = Food("Apple", "Red")

food_two = Apple("Banana", "Yellow")
food_two.eat()
food_one.eat()
print(food_one)
food_two.get_from_Tree()