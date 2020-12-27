from datetime import datetime
from pytz import timezone

tz = 'Africa/Johannesburg'
south_africa = timezone(tz)

currentdatetime = datetime.now(south_africa)
print(currentdatetime)
print(type(currentdatetime))

print(currentdatetime.day)
print(currentdatetime.month)
print(currentdatetime.year)

print(currentdatetime.hour)
print(currentdatetime.minute)
print(currentdatetime.second)

# pr = sa_time.strftime('%Y-%m-%d_%H-%M-%S')
# print(pr)
# print(type(pr))