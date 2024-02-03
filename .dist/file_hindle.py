import os
print(os.getcwd())
print(os.path.dirname(__file__))

with open(os.path.dirname(__file__) + '/test.txt', 'w') as f:
    f.write('hello world')