str1 = "Python Basics review from start to finish"
str2 = " after that pytest"

print(str1[1]) #y

#get substring
print(str1[0:5]) #Pyth

#reverse
print(str1[::-1]) #hsinif ot trats morf weiver scisaB nohtyP

#concatenate
print(str1 + str2)

#check if substring is present
print("basics" in str1)
print("basics" in str1.lower())

#split string
words = str1.split(" ") #creates a list of split strings
print(words)

str4 = "    great     "
#strip - remove whitespaces beginning and ending
print(str4.strip()) #removes leading and trailing spaces
print(str4.lstrip()) #removes leading spaces
print(str4.rstrip()) #removes trailing spaces