print("hello")
#this is how you put a one line comment
"""
this 
is 
a 
multiline 
code
"""
#int
a = 3
#string
Str = "this a string"
print(Str, a)

#multiple variable in a line
a, b, c = 1, 1.4, "string again"
print(a, b, c, sep=", ")

#print("Value is" + b)
print("{} {}".format("Value is", b))
#you can also do this
print("value is", b)
#and this
print(f"Value is {b}")

#to know the datatype
print(type(a), type(b),type(c))

"""
DATA TYPES

Numeric
    -int (100)
    -long (deprecated in python 3)
    -float (10.3425)
    -complex (100+3j)

List, Tuple and Dictionary
    - refer demo2.py
"""

print(type(100+3j))

