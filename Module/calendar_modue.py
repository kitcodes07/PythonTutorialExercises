from calendar import Calendar

class MyCalendar(Calendar):

    def count_weekday_in_year(self, year, weekday):
        day_counter = 0
        for month in range(1, 13):
            for week in Calendar.monthdays2calendar(self, year, month):
               if week[weekday][0] != 0:
                   day_counter += 1
        return day_counter

wd = MyCalendar()

print(wd.count_weekday_in_year(2019, 0))
print(wd.count_weekday_in_year(2000, 6))