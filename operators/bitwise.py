#!/usr/bin/python

# Bitwise Operators: &, |, ^, ~, >>, <<

a = input("enter first value:")
b = input("enter second value:")


print("Binary equivalent to {0} is:{1}".format(a, format(a, 'b')))
print("Binary equivalent to {0} is:{1}".format(b, format(b, 'b')))

# bitwise and '&'
print("============== Bitwise AND:& ==============")
res = a & b
print("{0}&{1} is:{2}".format(a,b,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))

# bitwise OR '|'
print("============== Bitwise OR:| ===============")
res = a | b
print("{0}|{1} is:{2}".format(a,b,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))

# bitwise XOR '|'
print("============== Bitwise XOR:^ ==============")
res = a ^ b
print("{0}^{1} is:{2}".format(a,b,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))

# One's Complementary '~'
print("============== One's Complementary:~ ======")
res = ~a 
print("~{0} is:{1}".format(a,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))

# Left Shify '<<'
print("============== Left Shift:<< ==============")
res = a << 1
print("{0}<<1 is:{1}".format(a,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))

# Right Shify '>>'
print("============== Right Shift:>> =============")
res = a >> 1
print("{0}>>1 is:{1}".format(a,res))
print("Binary equivalent to {0} is {1}".format(res, format(res, 'b')))