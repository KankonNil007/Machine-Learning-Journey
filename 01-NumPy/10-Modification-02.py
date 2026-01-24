import numpy as np

# .delete() - Deletes a value
# .delete(array, index)

arr1 = np.array([2,3,35,43,36,4])
newArr1 = np.delete(arr1, 4)

print(arr1)
print(newArr1)

# Delete in 2D array

arr2 = np.array([[2,4,5], [4, 7, 8]])
newArr2 = np.delete(arr2, 0, axis=1)

print(arr2)
print(newArr2)

# Array Stacking
# .vstack() - row wise
# .hstack() - column wise

arr3 = np.array([2,4,2,4,25])
arr4 = np.array([4,25,5,8,9])

newArr3 = np.vstack((arr3, arr4))
newArr4 = np.hstack((arr3, arr4))

print(newArr3)
print(newArr4)

# Array Spliting
# .split() - equal spliting
# .vsplit() - row wise
# .hsplit() - column wise

arr5 = np.array([2,4,2,4,25,5,8,9,5,4,2,7])

print(np.split(arr5, 2))