import numpy as np

# .isnan() - detects missing values

arr1 = np.array([1, 2, np.nan, 3, np.nan])

print(np.isnan(arr1))

# .nan_to_num() - replaces nan/ missing values

arr2 = np.array([1, 2, np.nan, 3, np.nan])
newArr2 = np.nan_to_num(arr2, nan= 0)

print(newArr2)

# .isinf - detects infinite values

arr3 = np.array([10, 20, np.inf])

print(np.isinf(arr3))

# Replaces infinte values
newArr3 = np.nan_to_num(arr3, posinf=1000) 


print(newArr3)