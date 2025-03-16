#Inheritance is inheriting the properties from super class
from classes import Calculator

class child(Calculator):
    num2 = 20

    def getClassVariable(self):
        return self.num + self.num2 + self.summation()
obj = child()
print("child's result:")
print(obj.getClassVariable())
