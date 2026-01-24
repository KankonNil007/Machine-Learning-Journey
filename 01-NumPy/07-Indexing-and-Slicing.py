import numpy as np

# Indexing - Accessing the values

arr1 = np.array([3,6,4,8])
arr2 = np.array([[2,3], [4,6]])

print(arr1[0])
print(arr2[1,0])

# Slicing
# array[start,stop,step]
arr3 = np.array([10,20,30,40,50,60])

print(arr3[1:4]) # Indexes 1 to 3
print(arr3[:4]) # Indexes 0 to 3
print(arr3[1:4:2]) # Indexes 1 to 3 jumps by 2
print(arr3[::-1]) # Rversed Array

# Fancy Indexing - Multiple Elements
arr4 = np.array([20,30,50,60])

print(arr4[[0,2,3]])

# Filtering Data - Boolean Masking
arr5 = np.array([20,30,50,60,100,150])

print(arr5[arr5 > 30])