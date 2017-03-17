import datetime
from datetime import timedelta
import time

element = "下午12:22 - 2017年2月15日"
element = element.replace("下午", "")
# timeArray = time.strptime(element, "%H:%M - %Y年%m月%d日")  # timestamp: 1488947880  type: <class 'int'>
# element = "2017-03-08 12:38:00"
# timeArray = time.strptime(element, "%Y-%m-%d %H:%M:%S")
# 2将"2011-09-28 10:00:00"转化为时间戳
# timestamp = int(time.mktime(timeArray))
# 格式化的字符串转换成Datetime
dt = datetime.datetime.strptime(element, "%H:%M - %Y年%m月%d日")
print("dt:", dt)
# 加上12小时
aDay = timedelta(days=0.5)
now = dt + aDay
# print(now.strftime('%Y-%m-%d'))
print("new now:", now)
element = str(now)
timeArray = time.strptime(element, "%Y-%m-%d %H:%M:%S")
# 2将"2011-09-28 10:00:00"转化为时间戳
timestamp = int(time.mktime(timeArray))
print("timestamp:", timestamp)



