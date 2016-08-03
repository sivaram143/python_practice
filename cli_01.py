#!/usr/bin/python 
# usage: ./cli.py <arg1> <arg2> ...<argn>

# importing sys module
import sys

total = len(sys.argv)

# to print command line arguments
print('No.of arguments:', total, 'arguments.')
print('Argument List:', str(sys.argv))

# printing script name
print ("script name: %s" % str(sys.argv[0]))

# to print all arguments
if total != 0:
    for i in range(total):
        print("Argument # %d : %s" % (i, str(sys.argv[i])))

def main():
    name = sys.argv[1] # first command line arguent
    print("Hello", name)


# __name__ is a global variable, that exists in all namespaces.
# entry point to your program
if __name__ == '__main__':
    main()