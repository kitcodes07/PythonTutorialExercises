class fib:
    def __init__(self, ln):
        self.__ln = ln
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__ln:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        p3 = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, p3
        return p3

for x in [1, 2, 3, 5, 10]:
    test = list(fib(x))
    print(test)
    for i in test:
        print(i, end=", ")
    print("")
