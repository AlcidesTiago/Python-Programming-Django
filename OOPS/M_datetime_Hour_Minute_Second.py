from datetime import datetime

currentdate = datetime.today()
# print(currentdate)
# print(type(currentdate))

# print(currentdate.hour)

print('This is the time:')
h = currentdate.strftime("%I-%M-%S-%p")

print(h)
# print(type(h))