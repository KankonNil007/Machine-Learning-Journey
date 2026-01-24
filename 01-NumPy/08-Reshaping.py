import numpy as np

# Reshaping - 1D to 2D, 2D to 3D
arr1 = np.array([10,20,30,40,50,60])

arr2 = arr1.reshape(3,2) # Row, Column
print(arr2)

# Using -1, Calculates missing dimensions

arr5 = arr1.reshape(-1, 3) # Calculates Row, column = 3
print(arr5)

# ravel() - 2D to 1D, 3D to 1D - view
# flatten() - 2D to 1D, 3D to 1D - copy

arr3 = np.array([[40,50,60], [70,30,50]])
print(arr3.ravel())
print(arr3.flatten())