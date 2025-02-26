from datetime import datetime, timedelta

today = datetime.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print(today)
print(tomorrow)
print(yesterday)

now = datetime.now()

new_time = now + timedelta(hours=1, minutes=30)
print(new_time)


date1 = datetime(2020, 12, 31)
date2 = datetime(2021, 1, 1)

print(date2 - date1)
print((date2 - date1).days)