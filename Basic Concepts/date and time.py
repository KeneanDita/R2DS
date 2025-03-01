from datetime import *

date = date(2025, 4, 5)
today = date.today()

time = time(12, 30, 4)
now = datetime.now()
print(now)

now = now.strftime("%H:%M:%S  %d-%m-%Y")
print(now)


targetDatetime = datetime(2026,1,2, 12,30,0)
currentDatetime = datetime.now()

if targetDatetime < currentDatetime:
    print("Target date has passed")
else:
    print("Target has not passed")