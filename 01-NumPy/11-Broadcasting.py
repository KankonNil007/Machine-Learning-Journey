import numpy as np

# A sample Example 

prices = np.array([100,200,300])
discount = 10

finalPrice = prices - (prices * discount / 100)
print(finalPrice)

# Single Value

arr1 = np.array([34,64,86])
newArr1 = arr1 * 3

print(newArr1)

# 1D to 2D

arr2 = np.array([[1,2,3], [4,5,6]])
arr3 = np.array([7,8,9])

newArr2 = arr2 + arr3 

print(newArr2)