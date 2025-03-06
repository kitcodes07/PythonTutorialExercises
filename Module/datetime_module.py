from datetime import date, time, datetime
import time as tm

"""
today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# replace, weekday and isoweekday method
# weekday: Mon - 0, Sun - 6
# isoweekday: Mon - 1, Sun - 7
b = date(1992, 11, 7)
print(b)
print(b.weekday())
print(b.isoweekday())

b = b.replace(1992, 12, 5)
print(b)
print(b.weekday())



timestamp = tm.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)

t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)



#time module
#sleep only accepts integer not float
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        tm.sleep(seconds)
        print('I slept well! I feel great!')

student = Student()
student.take_nap(5)


#ctime() function

timestamp = tm.time()
print(tm.ctime(timestamp))
tm.sleep(5)
print(tm.ctime())

#gmtime() and localtime()

#in UTC
st = tm.gmtime(timestamp)
print(st)
#in local time
print(tm.localtime(timestamp))

#asctime() and mktime()

#converts structtime object to a string
print(tm.asctime(st))
#converts structtime or tuple  to number of seconds since Unix epoch
#Unix Epoch January 1, 1970, at 00:00:00 UTC (Coordinated Universal Time)
print(tm.mktime((2019, 11, 4, 14, 34, 4, 0, 300, 0)))


dt = datetime.now()
print("Datetime:",dt)
print("Date:", dt.date())
print("Time:", dt.time())
print("Time:", dt.timestamp())
dt.date()
print(dt.strftime('%Y/%m/%d'))
print(dt.strftime('%Y-%m-%d'))
print()
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))
print(d.strftime('%Y-%m-%d'))


print()
#returns current 'local' date and time with tzinfo as None.
print("today:", datetime.today())

#same as today by default but we can specific tzinfo as an optional arg
print("now:", datetime.now())

#returns current 'UTC' date and time with tzinfo as None.
print("utcnow:", datetime.utcnow())
"""

##############################################



