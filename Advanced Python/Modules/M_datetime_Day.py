from datetime import date

currentdate = date.today()
print(currentdate)
print(type(currentdate))

print(currentdate.day)

d = currentdate.strftime("%d-%B-%Y")
d1 = currentdate.strftime("%A")
print(d)
print(d1)
print(type(d))

# import datetime
#
# print(dir(datetime))