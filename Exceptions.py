# # x = -10
# # if x < 0:
# #     raise Exception(f"The number {x} is negative")

# # else:
# #     print(f"The number {x} is positive")


# # print("Print Message After If condition")
# x = "10"
# if type(x) != int:
#     raise ValueError(f"The value {x} is not an integer")

# else:
#     print(f"The value {x} is an integer")

# print("Print Message After If condition")
try:
    number = int(input("Enter your Age:"))
    print(number)
except ValueError:
    print("Please enter a valid number")
