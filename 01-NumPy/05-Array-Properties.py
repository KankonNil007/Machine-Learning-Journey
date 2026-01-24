import numpy as np

arr1 = np.array([[1,3,6,9,4],
                 [2,5,3,4,6],
                 [6,8,9,7,0]])
print(arr1.shape) # (rows, columns)
print(arr1.size) # number of elements
print(arr1.ndim) # number of dimensions
print(arr1.dtype) # Type of data

arr2 = np.array([1.2, 2.4, 5.7])
arr3 = arr2.astype(int) # Changing the type
print(arr2)
print(arr3)

# Total Memory Used - nbytes
print(arr1.nbytes)

# Transposing a Array
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4.T)

# Real and Imaginary Part of Complex arrays
arr5 = np.array([3+4j, 6-4j])
print(arr5.real)
print(arr5.imag)