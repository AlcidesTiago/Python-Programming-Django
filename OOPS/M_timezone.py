from datetime import datetime
from pytz import timezone

tz = 'Africa/Luanda'

Angola = timezone(tz)

currentdate = datetime.now(Angola)

print()
print('Angola: Africa/Luanda')
print('Date:',currentdate.day,'-',currentdate.month,'-',currentdate.year)
print('Time:',currentdate.hour,':',currentdate.minute,':',currentdate.second)

# print(currentdate.month)
# print(currentdate.year)
# print(currentdate.hour)
# print(currentdate.minute)
# print(currentdate.second)
