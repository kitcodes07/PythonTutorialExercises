from os import strerror
try:
    #stream = open("/Volumes/Macintosh HD/Users/karliantagupa/Downloads/test.txt", "w")
    stream = open("test.txt", "a")
    #stream.write("got to believe in magic")
    stream.close()
except IOError as exc:
    print("Error on a file: ", strerror(exc.errno))

try:
    ccnt = lcnt = 0
    #stream = open("/Volumes/Macintosh HD/Users/karliantagupa/Downloads/test.txt", "w")
    stream = open("test.txt", "rt", encoding="utf=8")
    lines = stream.readlines(40)
    print(lines)
    while len(lines) != 0:

        lines = stream.readlines(40)
        print(lines)

    stream.close()
except IOError as exc:
    print("Error on a file: ", strerror(exc.errno))
