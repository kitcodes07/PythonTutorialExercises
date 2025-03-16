
greetings = "Good Morning"
#greetings = "Morning"

if greetings == "Morning":
    print("Condition Matched")
else:
    print(greetings)

#for loop
#iterates each and every element

obj = [i*2 for i in range(6)]
#obj = []
for i in obj:
    print(i, end=" ")
    break

else: #will be executed as long as the for loop didn't stop via break.
    print()
    print("Entered Else")

print("Done")

#while loop
i = 0
print("while loop")
while i < len(obj):

    if i == 2:
        i += 1
        continue #skip the remaining steps
    print(i, end=" ")
    print(obj[i])

    if i > 3:
        break #halts the loop
    i += 1
else: #will be executed as long as the while loop didn't stop via break.
    print("Entered else")
