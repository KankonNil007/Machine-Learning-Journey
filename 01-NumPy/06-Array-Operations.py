import numpy as np

arr1 = np.array([10,20,30,40,50])

# Scalar Operations
print(arr1 + 5) # Addition
print(arr1 * 5) # Multiplication
print(arr1 ** 2) # Exponentiation
print(arr1 / 5) # Division

# Vector Operations
arr2 = np.array([10,20,30,40,50])
print(arr1 + arr2) # Addition
print(arr1 * arr2) # Multiplication
print(arr1 / arr2) # Division

# Mathematical Functions
# np.pi = 3.1416 
arr3 = np.array([0, np.pi/2])

print(np.sin(arr3))
print(np.sqrt(arr2))

# Aggregation Functions

var1 = np.sum(arr1) # Total Sum of the Array
var2 = np.mean(arr1) # Average of the Array
var3 = np.min(arr1) # Minimum value of the Array
var4 = np.max(arr1) # Maximum value of the Array
var5 = np.std(arr1) # Standard Deviation of the Array
var6 = np.var(arr1) # Variance of the Array

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)


# Matrix Calculations

arr4 = np.array([[2,4,3], [5,7,9]])
print(arr4.sum(axis=0))  # column-wise
print(arr4.sum(axis=1))  # row-wise

# Matrix Multiplication
arr5 = np.array([[1,2], [4,6]])
arr6 = np.array([[8,2], [7,9]])

print(np.dot(arr5, arr6))
print(np.linalg.det(arr5)) # Determinant
print(np.linalg.inv(arr6)) # Inverse Matrix
