#!/usr/bin/python

# assigning string to variable
myStr = "python"

# printing string value
print(myStr)

# prints the length of Strings
print(len(myStr)) 

# print all characters in string with its index
for i in range(len(myStr)):
    print("{0}:{1}".format(i, myStr[i]))

# prints 1 to 5 characters
print(myStr[1:5]) 

# prints first to 4 characters
print(myStr[:4]) 

# prints 2 to last characters
print(myStr[2:]) 

# list existing string methods
print(dir(myStr)) 

# converts string to lowercase
print(myStr.lower()) 

# converts string to uppercase
print(myStr.upper())

# string split
myString = "Javascript, Python, Node"
a, b, c = myString.split(",")
print(a)
print(b)
print(c)


