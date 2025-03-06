def fibonacci(n):
    p1 = p2 = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            p3 = p1 + p2
            p1, p2 = p2, p3
            yield p3

for i in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(i)

