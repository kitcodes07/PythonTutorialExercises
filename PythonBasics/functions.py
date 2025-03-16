#In python, a function is a group of related statements to perform a specific task

#Function definition / declaration
def GreetME(name):
    print("Good morning {}!".format(name))

def AddIntegers(a=0, b=0):
    return a + b #returns the sum of both arguments

#Function call / invocation
GreetME("Kian")
print(AddIntegers())
print(AddIntegers(2,4))