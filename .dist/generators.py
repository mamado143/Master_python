# Generators - is a function with "yield" keyword Instead of "return"
# It Support Iteration and Return Generator Iterator.



def myGenerator():
    yield 1 
    yield 2
    yield 3

print(myGenerator())

for i in myGenerator():
    print(i)
