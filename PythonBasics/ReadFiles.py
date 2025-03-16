
for i in open("test.txt", "r"):
    print(i[0], end=" ")
print()
f = open("test.txt", "r")
#reads the whole file
#print(f.read())  #a b c d e

#read the file 4 characters at a time
#print(f.read(4)) # alph
#print(f.read(4)) # abet

#read line by line
#print(f.readline()) # alphabet\n
#print(f.readline()) #beautiful\n

#print line by line using while
# l = f.readline()
# while l != "":
#     print(l)
#     l = f.readline()

#readlines() will generate a list
lf = f.readlines()
for i in lf:
    print(i.strip())
f.close()
