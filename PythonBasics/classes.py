#classes are user defined blueprint or prototype
#self keyword is mandatory for calling variables and methods
#instance and class variables serves different purposes

class Calculator:
    num = 100 #Class variable
    #constructor is implicitly invoked if not created.

    def __init__(self, a = 0, b = 0):
        self.__a = a #instance variable
        self.__b = b
    def __str__(self):
        return f"{self.__a} ... {self.num}"
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return "can't divide number with zero"
    def summation(self):
        return self.add(self.__a,self.__b)

print(Calculator().num)
cal = Calculator(3,5)
a = 1
b = 0
print(cal.add(a,b))
print(cal.sub(a,b))
print(cal.mul(a,b))
print(cal.div(a,b))
print(cal.summation())