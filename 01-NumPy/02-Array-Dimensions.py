import numpy as np

# 1D Array (One Dimensional Array)
# Axes: 1
# Vector , Shape: (n,), arr[i]

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.shape)
print(arr1[2])
print("\n")

# 2D Array (Two Dimensional Array)
# Axes: 2
# Matrix , Shape: (r, c), arr[i][j]

arr2 = np.array([[1,2,3],
                [4,5,6]])
print(arr2)
print(arr2.shape)
print(arr2[1, 2])
print("\n")

# 3D Array (Three Dimensional Array)
# Axes: 3
# Tensor , Shape: (d, r, c), arr[i][j][k]

arr3 = np.array([[[1,2],
                [4,5]],
                
                [[5,6],
                 [2,4]]])
print(arr3)
print(arr3.shape)
print(arr3[0, 1, 1])