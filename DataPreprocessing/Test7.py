from datetime import datetime
from datetime import timedelta

now = datetime.now()
print("now:", now, ", type:", type(now))
aDay = timedelta(days=0.5)
now = now + aDay
# print(now.strftime('%Y-%m-%d'))
print("new now:", now)
