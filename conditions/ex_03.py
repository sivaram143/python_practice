#!/usr/bin/python

# program to check whether a given no '+ve' or '-ve'
num = input("Enter any number:")

if num == 0:
    print("{0} is equal to 0".format(num))
if num > 0:
    print("{0} is positive".format(num))
if num < 0:
    print("{0} is negative".format(num))