from datetime import datetime

currentdate = datetime.today()

print()
print('This the Time & Date:')

D = currentdate.strftime("      %d-%B-%Y")
d = currentdate.strftime("          %A")
T = currentdate.strftime("      %I-%M-%S-%p")

print(D)
print(d)
print(T)