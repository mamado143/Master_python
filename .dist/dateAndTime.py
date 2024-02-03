# -----------------------------
# -- Date and Time => Introduction
# -----------------------------

import datetime

print(datetime.datetime.now())
print("#" * 40)
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)

# print(datetime.datetime.min)
# # print(datetime.datetime.max)
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)
# print(datetime.time.min)
# print(datetime.time.max)

myBirthday = datetime.datetime(1987, 12, 21)
dateNow = datetime.datetime.now().year

print(myBirthday)
print(dateNow)

print(dateNow - myBirthday.year)