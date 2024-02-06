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

food_one = Food("Apple", "Red")

food_two = Apple("Banana", "Yellow")
food_two.eat()
print(food_one)