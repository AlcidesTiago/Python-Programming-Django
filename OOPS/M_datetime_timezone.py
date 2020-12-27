from datetime import datetime
from pytz import timezone

tz = 'Africa/Johannesburg'

South_Africa = timezone(tz)

currentdate = datetime.now(South_Africa)

# print(currentdate)
# print(type(currentdatetime))

print()
print('South_Africa: Africa/Johannesburg')
print('Date:',currentdate.day,'-',currentdate.month,'-',currentdate.year)
print('Time:',currentdate.hour,':',currentdate.minute,':',currentdate.second)

# print(currentdatetime.day)
# print(currentdatetime.month)
# print(currentdatetime.year)
# print(currentdatetime.hour)
# print(currentdatetime.minute)
# print(currentdatetime.second)

# pr = sa_time.strftime('%Y-%m-%d_%H-%M-%S')
# print(pr)
# print(type(pr))