#!/usr/bin/python

# Arithmetic Operators: +, -, *, /, %, **(exponent:power)

num1 = input("Enter first number:")
num2 = input("Enter second number:")

print("************* Arithmetic Operators *************")

print("Addition(+):{0}+{1}={2}".format(num1,num2,num1+num2))

if num1 > num2:
    res = num1 - num2
else:
    res = num2 - num1
print("Subtraction(-):{0}-{1}={2}".format(num1,num2,res))

print("Multiplication(*):{0}*{1}={2}".format(num1,num2,num1*num2))
if num2 == 0:
    res = "Infinity"
else:
    res = num1 / num2

print("Division(/):{0}/{1}={2}".format(num1,num2,res))

print("Modulus(%):{0}%{1}={2}".format(num1,num2,res))

print("Exponential(**):{0}**{1}={2}".format(num1,num2,num1**num2))