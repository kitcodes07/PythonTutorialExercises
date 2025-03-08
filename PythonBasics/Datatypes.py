"""
DATATYPES

Numeric
    -int (100)
    -long (deprecated in python 3)
    -float (10.3425)
    -complex (100+3j)

String
    -sequence of characters that represents a text
    -enclose in:
        '' or "" - for single line
        """ """ - multiline


list []
    -datatype that allows multiple values and datatypes
    -mutable (can be modified)
Tuple ()
    -datatype that allows multiple values and datatypes
    -immutable (can't be modified)

Dictionary { key:value}
    -in java it is called hashmap
"""

#NUMERIC
#int, float, complex
a, b, c= 1, 1.3, 100+3j
print(a, b, c) #1 1.3 (100+3j)
#check their datatypes
print(type(a), type(b), type(c)) #<class 'int'> <class 'float'> <class 'complex'>

#string
a = 'it\'s a'
b = "it's b"
c = """
    a
    multiline
    c
    """
print(a, b, c)
"""
    it's a it's b 
    a
    multiline
    c
"""


values = [1, 3, "test", 4, 5]
print(values, values[1], values[-1])
print(values[1:3]) #the last argument is exclusive

#insert values in a list
values.insert(3, "python")
print(values) #[1, 3, 'test', 'python', 4, 5]

#append values in a list
values.append("XXX")
print(values) #[1, 3, 'test', 'python', 4, 5, 'XXX']

#update value in a list
values[2] = "Basic"
print(values) #[1, 3, 'Basic', 'python', 4, 5, 'XXX']

#del an item in a list
del values[0]
print(values) #[3, 'Basic', 'python', 4, 5, 'XXX']

#del an a list
temp = values[:] #creates a copy of the list
print(temp) #[3, 'Basic', 'python', 4, 5, 'XXX']
print(temp is values) #Returns False
del temp # this will delete the whole list
#print(temp) #NameError: name 'temp' is not defined

temp = values # the temp will have the same reference as values; so we can say temp is values
print(temp is values) #Returns True
del temp[-1] #if you do this, the values in values list will be updated as well
print(values) #[3, 'Basic', 'python', 4, 5]

#TUPLES
val_tup = (1, 2, "kian", 4.5)
print(val_tup) #(1, 2, 'kian', 4.5)
print(val_tup[2]) #kian

#DICTIONARY
dic = {"a": 2, 4:"bcd", 1.3:["1", ".", "3"]}
print(dic) #{'a': 2, 4: 'bcd', 1.3: ['1', '.', '3']}
print(dic[1.3]) #['1', '.', '3']
print(dic["a"]) #2
print(dic[4]) #bcd

#Create dictionary dynamically
dict= {}
print(dict)
dict["first"] = 1
print(dict)
print(dict["first"])


