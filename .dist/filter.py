def checkNumber(num):
    if num < 10:
        return num



myNumber = [1, 0,8, 9, 19, 20, 1000, 10 ,12]
myResult = filter(checkNumber, myNumber)
for i in myResult:
    print(i)