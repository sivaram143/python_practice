#/usr/bin/python
# To get the length and size of variable

from sys import getsizeof # import sys module and get only one method
myVar = "python" # assign string to myVar

print("myVar=%s" %myVar) # print 'myVar'

print("Length:",len(myVar)) # prints length of 'myVar'

print("Size:", getsizeof(myVar)) # to get memory size of 'myVar'