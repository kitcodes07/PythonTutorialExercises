
string1 = input("enter s1:").lower()
string2 = input("enter s2:").lower()
pos=0
count=0
for ch in string1:
    pos = string2.find(ch,pos)
    if pos == -1:
        count += 1
        break
if count == 0:
    print("Yes")
else:
    print("No")
