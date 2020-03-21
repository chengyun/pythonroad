from datetime import datetime, date, time, timedelta
import calendar

weeknum, days = calendar.monthrange(2018, 2)  # weeknum days
print(weeknum, days)

cal = calendar.month(2016, 1)
print(cal)

curdate = date.today()
print(curdate)
now = datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

nowstr = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowstr)
dt = datetime.strptime("20181217 20:40:30", "%Y%m%d %H:%M:%S")
print(dt)

d = date(2018, 12, 17)
print(d)

t = time(20, 30, 30)
print(t)

dt = datetime(2018, 12, 17, 20, 30, 30)
print(dt)

dtd = dt.date()
dtt = dt.time()

ts = dt.timestamp()
print(ts)
unix_ts = int(ts)
print(unix_ts)
dt = datetime.fromtimestamp(unix_ts)
print(dt)

td = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)  # 没有年 月
print(td)
d2 = d + td
print(d2)
print(d2 - d)
print(d < d2)
