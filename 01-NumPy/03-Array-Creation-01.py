import numpy as np

# Defining an Array
arr1 = np.array([1, 2, 4, 8])
print(arr1)

# Defining a zeroes array
arr2 = np.zeros((5))
# arr3 = np.zeros((5, 2)) - 2D
# arr4 = np.zeros((2, 3, 2)) - 3D
print(arr2)
# print(arr3)
# print(arr4)

# Defining a ones array
arr5 = np.ones((5))
print(arr5)

# Defining a Empty array
# Random garbage values
# Faster than zeroes or ones array
arr3 = np.empty((4))
print(arr3)


# Defining a Custom Value Array
# .full((dimensions), value)
arr8 = np.full((2,2), 9)
print(arr8)

# Defining a Sequencial Array
# .arange(start, stop, step)
arr7 = np.arange(10, 25, 3)
print(arr7)