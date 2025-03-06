
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = "0" + s
    return s

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hh = hours
        self.__mm = minutes
        self.__ss = seconds


    def __str__(self):
        return two_digits(self.__hh) + ":" + \
                two_digits(self.__mm)+ ":" + \
                two_digits(self.__ss)

    def next_second(self):
        self.__ss += 1
        if self.__ss > 59:
            self.__ss = 0
            self.__mm += 1
            if self.__mm > 59:
                self.__mm = 0
                self.__hh += 1
                if self.__hh > 23:
                    self.__hh = 0


    def prev_second(self):
        self.__ss -= 1
        if self.__ss < 0:
            self.__ss = 59
            self.__mm -= 1
            if self.__mm < 0:
                self.__mm = 59
                self.__hh -= 1
                if self.__hh < 0:
                    self.__hh = 23


timer = Timer(22, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
timer.prev_second()
print(timer)
