strings = input("Input your birthday yyyyMMdd: ")
while True:
    total = sum(int(ch) for ch in strings)
    if total > 9:
        strings = str(total)
    else:
        break
print(total)