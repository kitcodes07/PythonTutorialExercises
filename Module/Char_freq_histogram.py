from os import strerror

fn = input("Please input the filename: ")
try:
    chars = {}
    for line in open(fn, "r"):
        for ch in line:
            if ch.isalpha():
                ch = ch.lower()
                if ch in chars:
                    chars[ch] += 1
                else:
                    chars[ch] = 1
    for key, value in chars.items():
        print(f"{key} -> {value}")
except IOError as e:
    print("Can't access the file:", strerror(e.errno))
    exit(e.errno)