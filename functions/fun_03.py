#!/usr/bin/python
# scope: local scope and global scope.
# local : scope within the function only
# global : able to access in entire program

# function with argument and return value
a, b = 10, 5
def sum(a,b):
    print("Local:",locals()) # prints the local variables (local scope)
    return a+b

print("Global:", globals()) # prints the global variables (global scope)
print("sum of %d and %d is %d"%(a, b, sum(a,b))) # calling function