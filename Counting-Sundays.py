import datetime
import calendar
 
def findDay(y,m,d):
    name = datetime.datetime(y,m,d).weekday()
    return (calendar.day_name[name])
sun = 0
 
for y in range(1901,2001):
    for m in range(1,13):
        if findDay(int(y),int(m),int(1))=="Sunday":
            sun+=1
            
print(sun)