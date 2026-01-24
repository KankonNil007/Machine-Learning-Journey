import numpy as np

# Array Insertion
# .insert(array, index, value, axis=None)
# axis=0 - row-wise, axis=1 = columnwise

arr1 = np.array([12,34,56,35,23,68])
arr2 = np.insert(arr1, 2, 100, axis=None)

print(arr1)
print(arr2)

# 2D Array - Insertion

arr3 = np.array([[10,20,39],[12,43,67]])
arr4 = np.insert(arr3, 1, [5,6], axis=1)

print(arr3)
print(arr4)

# .append() - used to add multiple values
# .append(array, [values])

arr5 = np.array([3,5,6,87,32])
arr6 = np.append(arr5, [5,7])

print(arr5)
print(arr6)

# Array Concatenation
# .concatenate((array1, array2), axis=None)

arr7 = np.array([1,4])
arr8 = np.array([0,4])

newArr1 = np.concatenate((arr7, arr8), axis=None)

print(newArr1)