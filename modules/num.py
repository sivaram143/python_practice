#!/usr/bin/python

"""
NumPy and SciPy are open-source add-on modules to Python that provide common
mathematical and numerical routines in pre-compiled, fast functions.The NumPy (Numeric Python)
package provides basic routines for manipulating large arrays and matrices of numeric data.

The central feature of NumPy is the array object class.

install: pip3 install numpy
"""

# importing numpy module
import numpy as np

# creates arr with numpy
arr = np.array([1,3,5])

# prints arr
print(arr)
# prints type of arr
print(type(arr))
# converts array into float
arr = np.array([1,3,5], float)
print(arr)
# prints the arr elements
print(arr[0])
print(arr[1])
print(arr[2])
# prints arr by slicing
print(arr[:1])
# multi dimensional array (matrix)
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
# prints 1st row, 2 col value
print(arr[0,1])
# prints 2nd row, 2 col value
print(arr[1,1])
# returns tuple with the size of each array
print(arr.shape)
# type of values are stored in array
print(arr.dtype)
# returns the length of the first axis
print(len(arr))
# prints the array with range as 1 to 10
arr = np.array(range(10))
print(arr)
# converts/reshapes array as 2 rows, 5 cols
arr = arr.reshape(2,5)
print(arr)
# prints the arr shape as tuple
print(arr.shape)




