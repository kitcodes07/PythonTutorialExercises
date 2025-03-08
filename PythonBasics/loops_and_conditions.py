
greetings = "Good Morning"
#greetings = "Morning"

if greetings == "Morning":
    print("Condition Matched")
else:
    print(greetings)

#for loop
#iterates each and every element

obj = [i*2 for i in range(5)]
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
    print(obj[i], end=" ")
    i += 1
    if i > 2:
        break
else: #will be executed as long as the while loop didn't stop via break.
    print("Entered else")
