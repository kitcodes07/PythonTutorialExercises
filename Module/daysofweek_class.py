class WeekDayError(Exception):
    pass


class Weeker:


    def __init__(self, day):
        self.__days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        if not self.__days.__contains__(day):
            raise WeekDayError
        self.__day = self.__days.index(day)

    def __str__(self):
        return self.__days[self.__day % 7]

    def add_days(self, n):
        self.__day += n
      

    def subtract_days(self, n):
        self.__day -= n




try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
