#!/usr/bin/python

# Relational Operators: ==, !=/<>, >, <, >=, <=

num1 = input("Enter first number:")
num2 = input("Enter second number:")

print("************* Relational Operators *************")

print("num1=", num1)
print("num2=", num2)

# equality '=='
if num1 == num2:
    print("{0} is equal to {1}".format(num1,num2))
else:
    print("{0} is not equal to {1}".format(num1,num2))
    
# greater than '>'
if num1 > num2:
    print("{0} is greater than equal to {1}".format(num1,num2))
else:
    print("{0} is not greater than equal to {1}".format(num1,num2))

# less than '<'
if num1 < num2:
    print("{0} is less than equal to {1}".format(num1,num2))
else:
    print("{0} is not less than equal to {1}".format(num1,num2))
    
# not equal '!='
if num1 != num2:
    print("{0} is not equal to {1}".format(num1,num2))
else:
    print("{0} is equal to {1}".format(num1,num2))

# not equal '<>'
# not support in python3
if num1 <> num2:
    print("{0} is not equal to {1}".format(num1,num2))
else:
    print("{0} is equal to {1}".format(num1,num2))