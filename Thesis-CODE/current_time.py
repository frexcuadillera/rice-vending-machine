import time
import serial
#from ServoBillAcceptor import *


ser = serial.Serial('/dev/ttyUSB0', 9600)

t = time.localtime()
global string
print("Insert bill  (50) | (80) | (100)")
#value = 50
value=ser.write(str.encode("Y"))
print(value)

if t.tm_mon == 1:
    month = "January"
elif t.tm_mon == 2:
    month = "February"
elif t.tm_mon == 3:
    month = "March"
elif t.tm_mon == 4:
    month = "April"
elif t.tm_mon == 5:
    month = "May"
elif t.tm_mon == 6:
    month = "June"
elif t.tm_mon == 7:
    month = "July"
elif t.tm_mon == 8:
    month = "August"
elif t.tm_mon == 9:
    month = "September"
elif t.tm_mon == 10:
    month = "October"
elif t.tm_mon == 11:
    month = "November"
elif t.tm_mon == 12:
    month = "December"

year = t.tm_year
date = t.tm_mday

if t.tm_hour > 12:
    am_pm = "PM"
    hour = t.tm_hour - 12
else:
    am_pm = "AM"
    hour = t.tm_hour
    
if t.tm_min < 10:
    minute = "0%s"%t.tm_min
else:
    minute = str(t.tm_min)

if t.tm_sec < 10:
    second = "0%s"%t.tm_sec
else:
    second = str(t.tm_sec)

string = "   P%s -             \t       %s %s, %s  \t   %s:%s:%s %s\n"\
 %(value, month, date, year, hour, minute, second, am_pm)
#return 0
f = open("transaction.txt", "a")
f.write(string)
f.close()
