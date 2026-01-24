import numpy as np

# Creating Random Values Array
# Used in Simulations & ML

# .rand - Random values between 0-1
arr1 = np.random.rand(3)
print(arr1)

# .randint - Random integer values
arr2 = np.random.randint(1, 10, size=(5))
print(arr2)

# Creating Arrays with specified data type
# Memory Efficient
arr3 = np.array([2,3,5], dtype=int)
print(arr3)

# Creating Matrices
# Used in Linear Algebra

# Creating Identity Matrices
# .eye(size)
arr4 = np.eye(3)
print(arr4)

# Creating Diagonal Matrices
# .diag()
arr5 = np.diag([1,2,3])
print(arr5)

# .linspace() - generating evenly spaced numbers over a specified interval
# .linspace(start, stop, num of points)
# Used in Signal Processing
arr6 = np.linspace(0, 10, 5)
print(arr6)