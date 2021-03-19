import time

t = time.localtime()

print("Insert bill (20) | (50) | (100)")
value = raw_input()

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

string = "P%s - %s %s, %s\t%s:%s:%s %s\n"\
%(value, month, date, year, hour, minute, second, am_pm)

f = open("transaction.txt", "a")
f.write(string)
f.close()
