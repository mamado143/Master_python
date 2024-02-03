from functools import reduce


# # 1 + 2 + 3 + 4 + 5
# def sumAll(num1, num2):
#     return num1 + num2


numbers = [1, 2, 3, 4, 5]

# result = reduce(sumAll, numbers)
result = reduce(lambda num1, num2: num1 + num2, numbers)
print(result)