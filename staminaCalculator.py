# Stamina Calculator for the popular game Puzzles and Dragons

from datetime import time
from datetime import datetime

# dungeonTime = time(3, 30)
# print dungeonTime
# print datetime.now()
# 
# dTime = dungeonTime - datetime.now()
# print dTime

dungeonTime = raw_input("Time your dungeon starts (Hour:Minutes AM/PM): ")
time2 = '2:30 PM'
FORMAT = '%I:%M %p'

dTime = datetime.strptime(dungeonTime, FORMAT) - datetime.strptime(time2, FORMAT)
print dTime
# print dTime.minute
# print dtime.hour
dMinutes = dTime.total_seconds() / 60

regen = dMinutes / 3
print "You will regenerate " + str(regen) + " stamina before your dungeon starts."