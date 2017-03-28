# Stamina Calculator for the popular game Puzzles and Dragons

from datetime import time
from datetime import datetime

# dungeonTime = time(3, 30)
# print dungeonTime
# print datetime.now()
# 
# dTime = dungeonTime - datetime.now()
# print dTime

time1 = '3:30 PM'
time2 = '2:30 PM'
FORMAT = '%I:%M %p'

dTime = datetime.strptime(time1, FORMAT) - datetime.strptime(time2, FORMAT)
print dTime
# print dTime.minute
# print dtime.hour
print dTime.total_seconds() / 60