from datetime import date


currentdate = date.today()
print(currentdate)
print(type(currentdate))

print(currentdate.month)
print(currentdate.year)
print(currentdate.day)

dwy = currentdate.strftime("%d/%B%Y")
print(dwy)
print(type(dwy))