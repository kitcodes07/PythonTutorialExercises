# read the file and store all the lines in the list
# reverse the list
# write the list back to the file
#read file default is "r" so no need to put "r", but you can still specify it if want.
with open("test.txt", "r") as infile: #no need to explicitly close the file
    listWords = infile.readlines()
    #listWords.reverse() #this is if you want to reverse the list
    #listWords = listWords[::-1] #this could be done to reverse the list

#writing file
with open("test.txt", "w") as outfile:
     #could be done by going through the reversed list
     for line in reversed(listWords):
         outfile.write("{}{}".format(line.strip(),"\n"))

