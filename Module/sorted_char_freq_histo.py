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

    ol = sorted(chars.keys(), key=lambda x: chars[x], reverse=True)
    """
    ol = [ i for i in chars.keys()]
    print(ol)
    for x in range(len(ol) - 1):
        y = x + 1
        while y < len(ol):
            if chars.get(ol[x]) < chars.get(ol[y]):
                ol[x], ol[y] =  ol[y], ol[x]
            y += 1
    """


except IOError as e:
    print("Can't access the file:", strerror(e.errno))
    exit(e.errno)

try:
    dst = open(f'{fn}.hist', "w")
    for i in ol:
        dst.write(f"{i} -> {chars.get(i)} \n")
    dst.close()
except IOError as e:
    print("Can't access the file:", strerror(e.errno))
    exit(e.errno)
