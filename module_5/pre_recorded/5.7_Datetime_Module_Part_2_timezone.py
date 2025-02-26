import pytz
from datetime import datetime
import time

dhaka = pytz.timezone('Asia/Dhaka')
utc = pytz.utc

print(dhaka)
print(utc)

now = datetime.now()
print(now)

print(now.astimezone(dhaka))
print(now.astimezone(utc))

start = datetime.now()
time.sleep(3)
end = datetime.now()

print(start - end)
