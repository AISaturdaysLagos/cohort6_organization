# -*- coding: utf-8 -*-
"""Numpy notebook

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XTZzWmjvN9Rz3SfQI_8FqRkpVIO9sKPG

# Numpy

#### Importing Numpy

To import an external Python library such as Numpy, use Python's import function. To save yourself some typing later on, you can give the library you import an alias. Here, we are importing Numpy and giving it an alias of np.
"""

import numpy as np

"""### Creating numpy array

# 1-D Array
"""

#The np.array function is used to create an array

#creating a 1 dimensional array

x = np.array([1, 2, 3, 4, 5]) 
x

#The shape property is usually used to get the current shape of an array
x.shape

"""# 2-D Array"""

# Creating a 2D arrays  
y = np.array([[1, 2], [3, 4], [5,6]]) 
y

y.shape

"""# 3-D Arrays"""

# Creating a 3D arrays  
z = np.array([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]) 
z

z.shape

"""# Numpy function"""

#Numpy has built-in functions for creating arrays and manipulating.
#arange is Used to create arrays with values in a specified range.
A = np.arange(25)
A

#To change the shape of an array
B = A.reshape(25,1)
C = B.reshape(5,5)
C

"""* Note: Before a reshape function will run successful, the multiplication of the two parameter supply to the function must be equal with multiplication of the shape of the original array you want to reshape.
For example: The shape of variable B is (25, 1) therefore 25 * 1 = 25
The two parameter supply to the reshape function is (5, 5), 5 * 5 = 25


"""

#zeros is used to create an array filled with zeros. 
#ones is used to create an array filled with ones
#random.randn is used to create an array filled with random normal entries

#1D array
np.zeros (3)
np.ones (3)
np.random.randn (3)

#2D array
np.zeros((2,5))
#np.ones ((2,5))
#np.random.randn ((2,5))

"""### Accessing elements of numpy array"""

#To access an element in a two-dimensional array, you need to specify an index for both the row and the column.
D = np.array([[5, 7, 8],[3, 5, 9]])
D

# note that for array numbering in numpy, it starts from zero
#Row 1, column 0 gives a scalar value
D[1,0]

#Row 1, column 2
D[1,2]happy meme template

"""### Basic Numpy Array Math Operations"""

s = np.array([[1,2,3],[4,5,6]])
t = np.array([[2,2,2],[3,3,3]])

#Transpose a matrix
s.T

#Elementwise addittion
np.add(s,t)

#Elementwise Subtraction
np.subtract(s,t)

#Elementwise Multiplication
np.multiply(s,t)