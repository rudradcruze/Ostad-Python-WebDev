import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

today = datetime.date.today()
today_time = datetime.datetime.now().time()
print(today)
print(today_time)


custom_datetime = datetime.datetime(2030, 2, 20, 10, 30, 0)
print(custom_datetime)

# Formate
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y-%m-%d %I:%M:%S %p"))
print(now.strftime("%Y-%m-%d %H:%M:%S %A"))
print(now.strftime("%Y-%m-%d %H:%M:%S %a"))
print(now.strftime("%Y-%m-%d %H:%M:%S %B"))
print(now.strftime("%Y-%m-%d %H:%M:%S %b"))
print(now.strftime("%Y-%m-%d %H:%M:%S %c"))
print(now.strftime("%Y-%m-%d %H:%M:%S %x"))
print(now.strftime("%Y-%m-%d %H:%M:%S %X"))

date_string = "2020-12-31 10:30:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)
